from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model

from .models import Todo
from .serializers import TodoSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
 
