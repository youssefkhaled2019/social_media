from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
 user_id=models.OneToOneField(User,on_delete=models.CASCADE)
 image=models.ImageField(default="default.jpg",upload_to="profile_pics")
 def __str__(self):
  return f'{ self.user_id.username} profile '
 

 def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            size=(300,300)
            img.thumbnail(size)
            img.save(self.image.path)
# unique email

User._meta.get_field('email')._unique = True
