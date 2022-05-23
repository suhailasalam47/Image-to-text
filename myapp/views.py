
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import FormView
from .forms import *


# Create your views here.

class HomeView(FormView):
    form_class = UploadForm
    template_name = 'index.html'
    success_url = '/'

    
    def form_valid(self, form):
        upload = self.request.FILES['file']
        return super().form_valid(form)

        