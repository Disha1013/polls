from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page – Django Project")
