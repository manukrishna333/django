from django.http import HttpResponse

def welcome_page(request):
    return HttpResponse("Welcome Page")
