from django.db import models
from User.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=128)

    participants = models.ManyToManyField(CustomUser, through='UserProjectRelation')

ROLE_OPTIONS = (
    ('1', 'owner'),
    ('2', 'developer'),
)

class UserProjectRelation(models.Model):
    user = models.ForeignKey(CustomUser)
    project = models.ForeignKey(Project)

    role = models.CharField(max_length=1,choices=ROLE_OPTIONS)
    date_joined = models.DateField(auto_now_add=True)
