"""trydjango19 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from accounts.views import (login_view, register_view, logout_view )
from posts.views import (page_about, page_landing ) 
from django.contrib import admin
from django.conf.urls import handler404, handler500
from markdownx import urls as markdownx
import notifications.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^posts/', include("posts.urls", namespace='posts')),  
    url(r'^forum/', include("forum.urls", namespace='forum')),  
    url(r'^', include("courts.urls", namespace='courts')),    
    url(r'^about/$', page_about, name='about'),
    # url(r'^$', page_landing, name='landing'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^profiles/', include('accounts.urls', namespace='accounts')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^markdownx/', include(markdownx)),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),

    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

# handler404 = myapp_viewss.error_404

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
