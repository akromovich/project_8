from django.db import models
from django.db import models



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250,blank=False,verbose_name="Название статьи")
    text = models.TextField(max_length=2000,blank=False,verbose_name='Текст статьи')


    def __str__(self):
        return self.title