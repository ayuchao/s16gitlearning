from django.shortcuts import render,HttpResponse

def happy(request):
    return HttpResponse("我问王思聪,钱是万能的吗,王思聪说:钱是万达的,修复了这个bug,钱是老男孩的了")


def happy2(reuqest):
    return HttpResponse("曾经我被人打趴下了,然后我发现躺着真舒服")

def wupeiqi(request):
    reutrn HttpResponse("我是吴佩琪,老男孩的银角大王")


def alex(request):
    return HttpResponse("你就打瞌睡吧,模拟面试的时候,看你尴尬不")

def dev(request):
    return HttpResponse("dev开发的代码在这里")

def development(request):
    return HtppResponse("万事开头难,中间也难,结尾也难")
# Create your views here.
print('测试分支冲突的代码')
