from django.db import models
#from django.contrib.auth import get_user_model


class Task(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    
    class Progress(models.IntegerChoices):
        TODO = 0, ("To Do")
        INPROGRESS = 1, ("In Progress")
        DONE = 2, ("Done")
        
    progress = models.IntegerField(
        choices=Progress.choices,
        default=Progress.TODO,
    )
    def __str__(self):
        return self.name
 