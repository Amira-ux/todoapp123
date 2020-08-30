from django.urls import path 
from .views import ListTodo,DetailTodo,UsrtDetail,UserList

urlpatterns = [
    path("users/",UserList.as_view()),
    path("users/<int:pk>/",UsrtDetail.as_view()),
    path("<int:pk>/",DetailTodo.as_view()),
    path("",ListTodo.as_view()),
]

