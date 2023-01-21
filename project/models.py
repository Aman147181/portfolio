from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    name= models.CharField(max_length=200)
    description = models.TextField(default='Lorem ipsum dolor, sit amet consectetur adipisicing elit. Alias, voluptas itaque nulla impedit sunt consequatur consectetur suscipit. Ad, porro ab explicabo dolorem quo, provident soluta quam quisquam error, nulla culpa.')
    thumbnail = models.ImageField(upload_to = 'static/images/')
    ispopolar = models.BooleanField(default=True)
    def __str__(self):
        return self.name



