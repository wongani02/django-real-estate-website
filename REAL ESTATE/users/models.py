from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# from phonenumber_field.formfields import PhoneNumberField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')
    bio = models.CharField(max_length=100, blank=True, default=False)
    location = models.CharField(max_length=100, blank=True, default=True)
    # phone_number = PhoneNumberField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    whats_app_link = models.URLField(blank=True, null=True)
    public_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
