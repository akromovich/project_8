from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index),
    path('post/<int:pk>',views.detail_post,name='post')
]