from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title
    
