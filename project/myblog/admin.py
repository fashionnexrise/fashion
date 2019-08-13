from django.contrib import admin
from myblog.models import UserProfile, Post

# Register your models here.
admin.site.register(UserProfile)

admin.site.register(Post)
