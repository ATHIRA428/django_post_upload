from django.urls import path
from .import views
# from .views import create_post,user_login
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup, name='signup'),
    path('post_list',views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('user_login/',views.user_login, name='login'),
    path('user_logout/',views.user_logout, name='logout'),

]

