from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    
    return HttpResponse('<h1> Bonjour le monde , tu me manques jonas</h1>')

# Create your views here.
def index(request):
    
    return render(request,'base.html')

