from django.db import models


# Create your models here.
class TeamMember(models.Model):
    image = models.ImageField(upload_to='team_images')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
