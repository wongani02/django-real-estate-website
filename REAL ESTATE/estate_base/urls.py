from django.urls import path
from . import views
from .views import HouseDetailView, HomeView, PropertyCreateView, PropertyUpdateView, PropertyDeleteView,\
    UserPropertiesView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('submit/new/', PropertyCreateView.as_view(), name='submit'),
    path('property_single/<int:pk>/update/', PropertyUpdateView.as_view(), name='update'),
    path('contact/', views.contact, name='contact'),
    # path('user/<str:username>/', views.user_properties, name='user_properties'),
    path('complete/', views.complete, name='complete'),
    # path('estate_properties/', PropertiesView.as_view(), name='estate_properties'),
    path('estate_properties/', views.properties, name='estate_properties'),
    path('property_single/<int:pk>/', HouseDetailView.as_view(), name='property_single'),
    path('user/<str:username>', UserPropertiesView.as_view(), name='user_properties'),
    path('property_single/<int:pk>/delete/', PropertyDeleteView.as_view(), name='delete'),
]
