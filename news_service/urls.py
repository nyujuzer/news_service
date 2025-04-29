"""
URL configuration for news_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, re_path
from .views import ArticleListAPIView, gen_articles, test_api_key

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', ArticleListAPIView.as_view(), name='satirical_articles'),
    # path('test', test_api_key, name='test_api_key'),
    path('test', test_api_key, name='test_api_key_with_param'),
    path('gen', gen_articles, name='gen_artickes'),
    re_path(r'^test\?api_key=(?P<api_key>.+)$', test_api_key, name='test_api_key_with_param'),
    re_path(r'^gen\?api_key=(?P<api_key>.+)$', test_api_key, name='test_api_key_with_param'),
]
