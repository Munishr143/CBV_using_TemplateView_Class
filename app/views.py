from typing import Any, Dict
from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.views.generic import TemplateView
from django.http import HttpResponse

# class cbv_html(TemplateView):
#     template_name='cbv_html.html'

# Dealing with context

class cbv_data(TemplateView):
    template_name='cbv_data.html'
    def get_context_data(self, **kwargs):
        EDCO=super().get_context_data(**kwargs)
        EDCO['name']='Munish'
        EDCO['age']=23
        return EDCO
    
#Dealing with Form

class cbv_form(TemplateView):
    template_name='cbv_form.html'

    def get_context_data(self, **kwargs):
        EDCO=super().get_context_data(**kwargs)
        TFO=Topic_Form()
        EDCO['TFO']=TFO
        return EDCO
    
    def post(self, request):
        TFD=Topic_Form(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Data is inserted sucessfully')
