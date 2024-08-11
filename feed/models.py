from django.db import models

# Create your models here.
class Menu(models.Model):
    users=models.CharField(max_length=20)
    def __str__(self):
        return self.users
