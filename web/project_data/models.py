from datetime import datetime as dt
from django.db import models


# Create your models here.
class Project(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    main_category = models.CharField(max_length=1024)
    currency = models.CharField(max_length=32)
    deadline = models.TimeField()
    goal = models.FloatField()
    launched = models.TimeField()
    pledged = models.IntegerField()
    state = models.CharField(max_length=64)
    backers = models.IntegerField()
    country = models.CharField(max_length=8)
    usd_pledged = models.FloatField()
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()

    def __str__(self):
        return '{}'.format(self.name)
