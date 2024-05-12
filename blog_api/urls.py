from django.urls import path
from . import views
from . import api_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('new_post/', views.create_post, name='create_post'),
    path('api/posts/<int:pk>/', api_views.PostDetailAPI.as_view(), name='edit_post'),
    path('api/posts/<int:pk>/delete/', api_views.PostDeleteAPI.as_view(), name='delete_post'),
    path('search/', views.search_posts, name='search_posts'),
]