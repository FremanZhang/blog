"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from article.views import home, detail, archive, about, search_tag, blog_search
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^(?P<post_id>\d+)/$', detail, name='detail'),
    url(r'^tag(?P<tag>\w+)/$', search_tag, name="search_tag"),
    url(r'^archive/$', archive, name='archive'),
    url(r'^about/$', about, name='about'),
    url(r'^search/$', blog_search, name='search'),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
]
