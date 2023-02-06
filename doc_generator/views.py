from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Here is Doc Generator Index</h1>')


def standard_tes(request):
    return HttpResponse('<h1>Here is a page for creating Standard TES contract</h1>')


def standard_customs(request):
    return HttpResponse('<h1>Here is page for creating Standard customs contract</h1>')