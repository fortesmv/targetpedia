from django.urls import path, include
from django.contrib import auth
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
	path('', TemplateView.as_view(template_name='home.html'), name='home'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('user/<username>/', views.bookmark_user,
        name='bookmarks_bookmark_user'),
	path('bookmarks/', views.bookmark_list, name='bookmarks_bookmark_list'),
	path('criar/', views.bookmark_create, name='bookmarks_bookmark_create'),
	path('editar/<pk>', views.bookmark_edit, name='bookmarks_bookmark_edit'),
]