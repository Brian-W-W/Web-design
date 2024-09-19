from django.template import loader
from django.shortcuts import render,redirect
from django.http import HttpResponse
from. models import Member




# Create your views here.
def index(request):
    group_members = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'group_members': group_members,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def master(request):
  template = loader.get_template('master.html')
  return HttpResponse(template.render())
    
    
def navigation(request):
  template = loader.get_template('nav.html')
  return HttpResponse(template.render())
    

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))