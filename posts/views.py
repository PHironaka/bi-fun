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

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm
from .models import Post


def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid() and request.user.is_authenticated():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
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
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	comments = instance.comments
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form":form,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active() #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
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
	return render(request, "post_list.html", context)





def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		p_tags = form.cleaned_data['p_tags']
		instance = form.save(commit=False)
		instance.save()
		for p_tag in p_tags:
			instance.tags.add(p_tag)
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)


def page_about(request, slug=None):
	context	= {
	"title": "About",
	"content": "Basketball Is Fun is a site with a distinct focused on the beautiful sport we all love: basketball."
	}
	return render(request, "pages/about.html", context)

def page_landing(request, slug=None):
	return render(request, "pages/landing.html")


def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")



class Meta(object):
    """
    Helper for building context meta object
    """
    _keywords = []
    _url = None
    _image = None

    def __init__(self, **kwargs):
        self.use_sites = kwargs.get('use_sites', settings.USE_SITES)
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.extra_props = kwargs.get('extra_props')
        self.extra_custom_props = kwargs.get('extra_custom_props')
        self.custom_namespace = kwargs.get('custom_namespace', settings.OG_NAMESPACES)
        self.keywords = kwargs.get('keywords')
        self.url = kwargs.get('url')
        self.image = kwargs.get('image')
        self.object_type = kwargs.get('object_type', settings.SITE_TYPE)
        self.site_name = kwargs.get('site_name', settings.SITE_NAME)
        self.twitter_site = kwargs.get('twitter_site')
        self.twitter_creator = kwargs.get('twitter_creator')
        self.twitter_card = kwargs.get('twitter_card')
        self.facebook_app_id = kwargs.get('facebook_app_id')
        self.locale = kwargs.get('locale')
        self.use_og = kwargs.get('use_og', settings.USE_OG_PROPERTIES)
        self.use_twitter = kwargs.get('use_twitter', settings.USE_TWITTER_PROPERTIES)
        self.use_facebook = kwargs.get('use_facebook', settings.USE_FACEBOOK_PROPERTIES)
        self.use_googleplus = kwargs.get('use_googleplus', settings.USE_GOOGLEPLUS_PROPERTIES)
        self.use_title_tag = kwargs.get('use_title_tag', settings.USE_TITLE_TAG)
        self.gplus_type = kwargs.get('gplus_type', settings.GPLUS_TYPE)
        self.gplus_publisher = kwargs.get('gplus_publisher', settings.GPLUS_PUBLISHER)
        self.gplus_author = kwargs.get('gplus_author', settings.GPLUS_AUTHOR)
        self.fb_pages = kwargs.get('fb_pages', settings.FB_PAGES)
        self.og_app_id = kwargs.get('og_app_id', settings.FB_APPID)	