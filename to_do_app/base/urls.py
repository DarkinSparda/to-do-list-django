from django.urls import path
from . import views



# app_name = 'base'

urlpatterns = [
    path('', views.list, name='list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='task-create'),
    path('update/<int:pk>', views.update, name='task-update'),
    path('delete/<int:pk>', views.delete, name='task-delete'),
]