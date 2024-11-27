from django.shortcuts import render

def home(request):
    return render(request,'main/index.html',)


def about(request):
    return render(request, 'main/about.html')


def todolist(request):
    return render(request, 'main/todolist.html')


def finance(request):
    return render(request, 'main/finance.html')


def reg(request):
    return render(request,'main/reg.html')


def log(request):
    return render(request,'main/log.html')


def acc(request):
    return render(request,'main/acc.html')