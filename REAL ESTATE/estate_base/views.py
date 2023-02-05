from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .filters import PropertyFilters
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from users.models import Profile
import json

# Create your views here.


class HomeView(ListView):
    template_name = 'estate_base/home.html'
    model = HouseDetails
    context_object_name = 'property_details'

def complete(request):
    body = json.loads(request.body)
    product = HouseDetails.objects.get(id=body[
        'productID'
    ])
    print(product)
    user = HouseDetails.objects.get(name=body[
        'user'
    ])


class HouseDetailView(DetailView):
    template_name = 'estate_base/property.html'
    model = HouseDetails
    context_object_name = 'property_details'

#     def get_object(self, queryset=None):
#         obj = super(HouseDetailView, self).get_object()
#         return obj
#
#     def get_context_data(self, **kwargs):
#         context = super(HouseDetailView, self).get_context_data()
#         context['houseDetails'] = HouseDetails.ojects.all()
#         context['profileDetails'] = Profile.objects.all()
#         return context


def properties(request):

    house_details = HouseDetails.objects.all().order_by('-date_created')
    filtered_property = PropertyFilters(request.GET, queryset=house_details)
    house_details = filtered_property.qs
    page = Paginator(house_details, 12)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
        'filtered_property': filtered_property,
        # 'house_details': house_details,
    }

    return render(request, 'estate_base/properties_2.html', context)


class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = HouseDetails
    context_object_name = 'property'
    fields = ['property_name', 'description', 'status', 'number_of_bedrooms', 'price', 'phone_number', 'location',
              'number_of_bathrooms', 'house_number', 'garages', 'house_images', 'area', 'district', 'image_2', 'image_3'
            , 'property_authentication']
    template_name = 'estate_base/submit-property.html'

    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)


class PropertyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = HouseDetails
    context_object_name = 'property'
    fields = ['property_name', 'description', 'status', 'number_of_bedrooms', 'price', 'location', 'number_of_bathrooms'
        , 'phone_number', 'house_number', 'garages', 'house_images', 'area', 'district']
    template_name = 'estate_base/submit-property.html'

    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.agent:
            return True
        return False


class PropertyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = HouseDetails
    template_name = ''
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.agent:
            return True
        return False


class UserPropertiesView(ListView):
    template_name = 'estate_base/user-properties.html'
    model = HouseDetails
    ordering = ['-date_created']
    context_object_name = 'property_details'
    paginate_by = 30

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return HouseDetails.objects.filter(agent=user).order_by('-date_created')

    # def test_func(self):
    #     post = self.get_context_object_name(object_list='property_details')
    #     if self.request.user == post.user:
    #         return True
    #     return False


def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'first_name': first_name,
            'lastname': last_name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(email, message, '', ['wonganitemborgb2@gmail.com'])
        # print(data)
        return render(request, 'estate_base/contact.html')
    else:
        return render(request, 'estate_base/contact.html')
