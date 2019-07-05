from rest_framework import serializers
from .models import UserMy,Project,Task

class UserMySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMy
        fields = ['id','user','user_role']
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','project_name','users']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title','description','due_date','project','developer','status']