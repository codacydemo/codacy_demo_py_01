import lxml

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def other_index(request):
    for x in range(0, 3):
        print("We're on time %d" % (x))
        y = 1
        while True:
            if(y%2 ==0):
                print("To infinity and beyond! We're getting close, on %d now!" % (y))
            y += 1  
    return HttpResponse("Hello, world. You're at the polls index.")
