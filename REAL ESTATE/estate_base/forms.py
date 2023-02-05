from django.forms import ModelForm
from .models import *


class SubmitPropertyDetailsForm(ModelForm):
    class Meta:
        model = HouseDetails
        fields = ['property_name', 'description', 'status', 'number_of_bedrooms', 'price', 'location', 'number_of_bathrooms',
                  'house_number', 'garages', 'house_images', 'area', 'district']


# class SubmitImagesForm(ModelForm):
#     class Meta:
#         model = PropertyImages
#         fields = ['images']
