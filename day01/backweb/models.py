from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=120)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'