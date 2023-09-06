from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('upload/', views.upload_photo, name='upload'),
    path('delete/<int:pk>/', views.delete_photo, name='delete_photo'),
]