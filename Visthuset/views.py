'''
Created on 16 okt. 2016

@author: Adrian
'''
# Create landing view
from django.views.generic.base import TemplateView

class LandingView(TemplateView):
    template_name = "landing.html"