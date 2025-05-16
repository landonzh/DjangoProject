from django.urls import path
from . import views
urlpatterns = [
    path('add-user/', views.add_user, name='add_user'),
    path('list-users/', views.list_users, name='list_users'),
    path('edit-user/<str:user_id>/', views.edit_user, name='edit_user'),
    path('', views.home, name='home'),
    path('players/', views.players, name='players'),
    path('champions/', views.champions, name='champions'),
    path('fanzone/', views.fanzone, name='fanzone'),
    path('rules/', views.rules, name='rules'),
    path('highlights/', views.highlights, name='highlights'),
    path('login/', views.login, name='login'),

]