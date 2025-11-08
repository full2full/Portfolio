from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, 'myapp/index.html')
def project(request):
    return render(request, 'myapp/project.html')
def contact(request):
    return render(request, 'myapp/contact.html')


