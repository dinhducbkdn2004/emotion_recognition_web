from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def users(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())