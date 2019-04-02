from django.http import HttpResponse


def index(request):
    a = "first line"
    b = "second line"
    c = "other line..."
    return HttpResponse("Hello, world. You're at the polls index.")


def other_index(request):a = "first line"
    a = "first line"
    b = "second line"
    c = "other line..."
    return HttpResponse("Hello, world. You're at the polls index.")