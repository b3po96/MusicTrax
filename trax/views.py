from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, you've reached the index for the site!")
