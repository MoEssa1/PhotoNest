from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    x = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    profile_picture = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.user.username


# Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Photo Model
class Photo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    caption = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.caption[:20]} - {self.date_uploaded}'
