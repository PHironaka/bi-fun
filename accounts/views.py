from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from .forms import UserLoginForm, UserRegisterForm




def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("/")
    return render(request, "account/login.html", {"form":form, "title": title})


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
    
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "account/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")



User = get_user_model()
class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

class UserListView(ListView):
    """docstring for UserListView"""
    template_name = 'user_list.html'
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

def user_delete(request, slug=None):
    if not request.user:
        raise Http404
    object = get_object_or_404(User, slug=slug)
    object.delete()
    messages.success(request, "Successfully deleted")
    return redirect("court:list")