from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
   x = 1
   x = 2 

   #return render(request,'hello.html', {'name': 'mosh'})
   return HttpResponse('Hello World')

#pull data from db
# transform
#send email 








# Create your views here.
# request -> response 
# request handler 