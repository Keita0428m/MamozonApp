from django.shortcuts import render

# Create your views here.
from django.views import generic 

class Lp(generic.TemplateView):
    template_name = 'mamozon/lp.html'
