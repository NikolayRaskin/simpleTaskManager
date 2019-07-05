from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserMy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=40, choices=(('Manager','Manager'),('Developer','Developer')))
    def __str__(self):
        return self.user.username
    
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    users = models.ManyToManyField(UserMy)
    def __str__(self):
        return self.project_name
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    project = models.ForeignKey('Project',on_delete=models.PROTECT)
    developer = models.ForeignKey('UserMy',on_delete=models.PROTECT,limit_choices_to={'user_role': 'Developer'})
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title