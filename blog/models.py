from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    # P_ID=models.
    title=models.CharField(max_length=20)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
    
    
    
    
#auto_now=True update date every time post update 
# auto_now_add==True add time now when data created  only not change in update 