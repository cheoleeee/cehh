from django.contrib import admin
from django.urls import path 
from . import views 

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), 
    path('renew/<int:blog_id>/', views.renew, name='renew'), 
    path('recreate/<int:blog_id>/', views.recreate, name='recreate'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('newblog/', views.blogpost, name="newblog"),
]

