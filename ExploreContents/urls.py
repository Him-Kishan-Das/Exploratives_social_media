from django.urls import path
from .import views

urlpatterns = [
    path('', views.signup),
    path('login/', views.login_page, name='login'),
    path('logout/', views.my_logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('submit_post', views.newPost),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('submit_post/', views.newPost)
]
#   