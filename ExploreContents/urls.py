from django.urls import path
from .import views

urlpatterns = [
    path('', views.signup),
    path('login/', views.login_page, name='login'),
    path('logout/', views.my_logout_view, name='logout'),
    path(f'profile/<str:username>/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('submit_post/', views.newPost),
    path('like-btn/', views.like),
    path('comment-btn/', views.comment)
]
