from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from application import tests


@csrf_exempt

def getVideo(request):
    if request.method == 'GET':
        return render(request,'../templates/index.html')
    if request.method == 'POST':
        image = request.FILES['image'].name
        print("Views",image,type(image))
        response = tests.getVideoPath(image)
        print(response)
        return render(request,'../templates/response.html',{"r":response})