from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(null=True)


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

class Apointments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Feedback(models.Model):
    feedback = models.CharField(max_length=100)
