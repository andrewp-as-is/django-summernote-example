from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from apps.blog.views import PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', PostListView.as_view(), name='post_list'),
]
