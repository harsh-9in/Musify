from django.db import models

# Create your models here.

class Room(models.Model):
    code=models.CharField(max_length=8,unique=True,default="")
    host=models.CharField(max_length=40,unique=True)
    guest_can_pause=models.BooleanField(default=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.host

