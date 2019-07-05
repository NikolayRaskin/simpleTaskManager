from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('users', UserView)
router.register('projects', ProjectView)
router.register('tasks', TaskView)


urlpatterns = [
    path('', main, name='mainPage'),
    #path('docs/', include('rest_framework_docs.urls')),
    path('addTask/',addTaskForm,name='addTask'),
    path('deleteTask/',deleteTask_view,name='deleteTask'),
    path('editTask/<task_id>',editTask_view,name='editTask'),
    path('compliteTask/<task_id>',compliteTask_view,name='compliteTask'),
    
    path('rest_api/',include(router.urls))
]
