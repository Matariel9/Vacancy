from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your mod els here.
class User(AbstractUser):
    SEX = [("m", "Male"), ("f","Female")]
    sex = models.CharField(max_length = 1,choices = SEX, default = "m")
