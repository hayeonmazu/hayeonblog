"""hayeon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import hblog.views ,portfolio.views

urlpatterns = [
    path('blog/<int:blog_id>',hblog.views.detail, name="detail"),
    path('', hblog.views.home , name="home"),
    path('admin/', admin.site.urls),
    path('blog/new/',hblog.views.new, name="new"),
    path('blog/create',hblog.views.create, name="create"),
    path('portfolio/portfolio',portfolio.views.portfolio, name="portfolio"),
]
