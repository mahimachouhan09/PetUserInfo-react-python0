from django.urls import path
from . import views

# app_name = 'petapi'
urlpatterns = [
    # path('index/', views.index, name='index'),
    path('users/', views.UserList.as_view()),
    path('pets/', views.PetList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('pets/<int:pk>/', views.PetDetail.as_view()),
]