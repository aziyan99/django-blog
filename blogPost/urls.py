from . import views
from django.urls import path

url_patterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path(r'^about/$', 'views.about', name='about'),

]
