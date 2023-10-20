from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


app_name = 'landmark'

urlpatterns = [
    path('', views.first, name='first'),
    path('index/', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('info/<int:id>/', views.file_info, name='info'),
    path('delete/<int:id1>/', views.delete_file, name='delete'),
    path('result/<int:id>/', views.result, name='result'),
    path('list/<int:id>/', views.file_list, name='list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('intro/', views.intro, name='intro'),
]
