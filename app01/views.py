from django.shortcuts import render,HttpResponse

def happy(request):
    return HttpResponse("我问王思聪,钱是万能的吗,王思聪说:钱是万达的,修复了这个bug,钱是老男孩的了")


def happy2(reuqest):
    return HttpResponse("曾经我被人打趴下了,然后我发现躺着真舒服")
# Create your views here.
