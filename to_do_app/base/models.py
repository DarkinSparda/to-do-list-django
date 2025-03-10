from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, validators=[MinLengthValidator(5, 'Description must be more than 5 characters')])
    complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name