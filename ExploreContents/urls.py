from django.urls import path
from .import views

urlpatterns = [
    path('', views.signup),
    path('submit_post', views.newPost),
    path('home/', views.home),
    path('profile/', views.profile),
    path('login/', views.login_page),
    path('submit_post/', views.newPost)
]
