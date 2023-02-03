from django.db import models
from django.contrib.auth.models import User
# Create your models here.

gender_choices = [
    ('.......', '.......'),
    ('male', 'male'),
    ('female', 'female'),
]


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=gender_choices)
    
    def __str__(self):
        return self.username
    
    
class Predict(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    last_date = models.DateField()
    
    def __str__(self):
        return self.owner