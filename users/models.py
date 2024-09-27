from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
 user_id=models.OneToOneField(User,on_delete=models.CASCADE)
 image=models.ImageField(default="default.jpg",upload_to="profile_pics")
 def __str__(self):
  return f'{ self.user_id.username} profile '
 


# unique email

User._meta.get_field('email')._unique = True
