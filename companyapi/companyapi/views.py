
from django.http import HttpResponse

def home_page(request):
    print("home page rewuested")
    return HttpResponse("<h1>This is Home Page</h1>")