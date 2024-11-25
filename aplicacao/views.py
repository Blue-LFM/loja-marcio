from django.shortcuts import render

def index(request):
    return render(request, 'aplicacao/index.html')
       
def index2(request):
    return render(request, 'aplicacao/index2.html')

def index3(request):
    return render(request, 'aplicacao/index3.html')

def index4(request):
    return render(request, 'aplicacao/index4.html')

def index5(request):
    return render(request, 'aplicacao/index5.html')
