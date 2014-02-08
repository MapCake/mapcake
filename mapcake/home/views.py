from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
	template = TemplateResponse(request,'home/index.html',{})
	return template

def layers(request):
	template = TemplateResponse(request,'home/layers.html',{})
	return template