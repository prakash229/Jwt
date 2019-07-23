from django.shortcuts import render
from .models import *
# Create your views here.
from django.views.generic import FormView
from django.http import JsonResponse
from .forms import RegistrationForm

class UserRegistrationView(FormView):
    form_class = RegistrationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        UserManager.objects.create_user(username, password=password)
        res_data = {
            'error': False,
            'message': 'Success, Please login'
        }
        return JsonResponse(res_data)

    def form_invalid(self, form):
        res_data = {
            'error': True,
            'errors': form.errors
        }
        return JsonResponse(res_data)