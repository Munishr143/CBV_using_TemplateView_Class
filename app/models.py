from django.db import models

# Create your models here.

class Topic(models.Model):
    S_No=models.IntegerField(primary_key=True)
    Topic_Name=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.Topic_Name
