from django.contrib import admin
from .models import Article, User, API_keys 

admin.site.register(Article)
admin.site.register(User)
admin.site.register(API_keys)