from django.shortcuts import render,HttpResponse

def happy(request):
    return HttpResponse("我问王思聪,钱是万能的吗,王思聪说:钱是万达的")

# Create your views here.
