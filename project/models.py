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

class Comment(models.Model):
    project=models.ForeignKey(Projects,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body= models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_date']
    
    def __str__(self):
        return '%s -  %s' %(self.project.name,self.user.username)

