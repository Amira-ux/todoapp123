from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
          model=Todo
          fields=("id","title","body")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=("id","username")
               