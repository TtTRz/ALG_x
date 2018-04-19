from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'ALG_web/home.html')
