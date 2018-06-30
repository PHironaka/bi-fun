try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.signals import post_save
from notifications.signals import notify
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import RedirectView
from comments.forms import CommentForm
from comments.models import Comment
from .forms import CourtForm
from .models import Court
from django.views.generic import DetailView, ListView
from taggit.models import Tag
from django.contrib.sitemaps import Sitemap


  

   	
def court_create(request):
	if not request.user:
		raise Http404
		
	form = CourtForm(request.POST or None, request.FILES or None)
	title = "Create Court"
	if form.is_valid() and request.user.is_authenticated():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()
		# message success
		messages.success(request, "<a href='#'> Court Created</a> ", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "court_form.html", context)

def court_detail(request, slug=None):
	instance = get_object_or_404(Court, slug=slug)
	share_string = quote_plus(instance.content)

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid() and request.user.is_authenticated():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()

		

		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,

						)
		# notify.send(request.user, verb='new comment!')
# 		notify.send(, recipient=request.user, verb='replied', action_object=comment,
# description=comment.comment, target=comment.content_object)

		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	comments = instance.comments
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form":form,
	}
	return render(request, "court_detail.html",  context)



def court_list(request):
	today = timezone.now().date()
	obj = Court.objects.active() #.order_by("-timestamp")

	if request.user:
		obj = Court.objects.all()
	
	query = request.GET.get("q")
	if query:
		obj = obj.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(obj, 10) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, "court_list.html", context)



def court_update(request, slug=None):
	if not request.user:
		raise Http404
	instance = get_object_or_404(Court, slug=slug)
	form = CourtForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form.save_m2m()
		messages.success(request, "<a href='#'> Saved</a> ", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "court_form.html", context)



def court_delete(request, slug=None):
	if not request.user:
		raise Http404
	instance = get_object_or_404(Court, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("court:list")

class courtLikeToggle(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		slug = self.kwargs.get("slug")
		print(slug)
		obj = get_object_or_404(Court, slug=slug)
		url_ = obj.get_absolute_url()
		user = self.request.user
		if user.is_authenticated():
			if user in obj.likes.all():	
				obj.likes.remove(user)
			else:	
				obj.likes.add(user)
		return url_

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class TagIndexView(ListView):
    template_name = 'tags/tag_detail.html'
    model = Court
    paginate_by = '10'
    context_object_name = 'courts'

   

    def get_queryset(self):
        return Court.objects.filter(tags__slug=self.kwargs.get('slug'))



class courtLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


   
    def get(self, request, slug=None, format=None):
        obj = get_object_or_404(Court, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated():
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)


class CourtSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Entry.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date



    # def get_paginate_by(self, queryset):
    #     paginate_by = Blog.objects.get_blog().entries_per_page
    #     return paginate_by

    # def get_context_data(self, *args, **kwargs):
    #     context = super(TagDetails, self).get_context_data(**kwargs)
    #     context['tag'] = self.kwargs['tag']
    #     return context


