from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# from phonenumber_field.formfields import PhoneNumberField

# Create your models here.


class HouseDetails(models.Model):

    STATUS = (('Sale', 'Sale'),
              ('Rent', 'Rent'),
              ('Guest wing', 'Guest wing'),
              )

    DISTRICTS = (('Lilongwe', 'Lilongwe'),
                 ('Blantyre', 'Blantyre'),
                 ('Zomba', 'Zomba'),
                 ('Mzuzu', 'Mzuzu'),
                 ('Salima', 'Salima'),
                 ('Mangochi', 'Mangochi'),
                 ('Mulanje', 'Mulanje'),
                 ('Mzimba', 'Mzimba'),
                 ('Dedza', 'Dedza'),
                 ('Dowa', 'Dowa'),
                 ('Machinga', 'Machinga'),
                 ('Balaka', 'Balaka'),
                 ('Chikhwawa', 'Chikhwawa'),
                 ('Kasungu', 'Kasungu'),
                 ('Thyolo', 'Thyolo'),
                 ('Phalombe', 'Phalombe'),
                 ('Rumphi', 'Rumphi'),
                 ('Chitipa', 'Chitipa'),
                 ('Neno', 'Neno'),
                 ('Nsanje', 'Nsanje'),
                 ('chiradzulu', 'Chiradzulu'),
                 ('Karonga', 'Karonga'),
                 ('Nkhata-Bay', 'Nkhata-Bay'),
                 ('Nkhotakota', 'Nkhotakota'),
                 ('Ntchisi', 'Ntchisi'),
                 ('Ntcheu', 'Ntcheu'),
                 ('Mchinji', 'Mchinji'),
                 ('Mwanza', 'Mwanza'),
                )

    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=300, null=True)
    status = models.CharField(null=True, choices=STATUS, max_length=200)
    number_of_bedrooms = models.PositiveSmallIntegerField(null=True)
    date_created = models.DateTimeField(default=timezone.now)
    price = models.FloatField(null=True)
    location = models.CharField(max_length=300, null=True)
    number_of_bathrooms = models.PositiveSmallIntegerField(null=True)
    house_number = models.CharField(max_length=50, null=True)
    garages = models.PositiveSmallIntegerField(null=True)
    house_images = models.ImageField(null=True, upload_to='house_images/')
    area = models.FloatField(null=True)
    district = models.CharField(max_length=100, null=True, choices=DISTRICTS)
    property_authentication = models.FileField(null=True, blank=False)
    phone_number = models.CharField(max_length=50, null=True)
    image_2 = models.ImageField(null=True, upload_to='house_images/')
    image_3 = models.ImageField(null=True, upload_to='house_images/')

    def __str__(self):
        return self.property_name

    def get_absolute_url(self):
        return reverse('property_single', kwargs={'pk': self.pk})


class ContactDetails(models.Model):
    twitter_link = models.URLField(null=True)
    instagram_link = models.URLField(null=True)
    facebook_link = models.URLField(null=True)
    whatsapp_link = models.URLField(null=True)
    phone_number = models.CharField(null=True, max_length=50)
    phone_number_2 = models.CharField(null=True, max_length=50)
    email = models.EmailField(null=True)
    location = models.CharField(max_length=100, null=True)
