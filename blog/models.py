from django.db import models
from author.models import *
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=50)
    content=models.TextField()
    slug=models.CharField(max_length=30)
    tiemStamp=models.DateTimeField(blank=True)
    # au=models.OneToOneField(
    #     Author,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
        
    # )
    
    def __str__(self):
        return  self.title +' by '+self.author

