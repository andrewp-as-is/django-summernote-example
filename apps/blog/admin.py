from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

"""
https://github.com/summernote/django-summernote
"""

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)
