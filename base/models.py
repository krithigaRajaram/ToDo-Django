from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class List(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    content = models.TextField(null=True,blank=True) 
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
   
    
    class Meta:
       ordering=['-updated','-created']  

    def __str__(self):
        return self.content
