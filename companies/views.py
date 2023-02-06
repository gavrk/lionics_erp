from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Here is a list of existing companies</h1>')


def register_loc(request):
    return HttpResponse('<h1>Here is a page for creation of new LOCAL companies</h1>')


def edit_or_delete_loc(request):
    return HttpResponse('<h1>Here is a page for editing or deleting existing LOCAL companies</h1>')


def register_int(request):
    return HttpResponse('<h1>Here is a page for creation of new INTERNATIONAL companies</h1>')


def edit_or_delete_int(request):
    return HttpResponse('<h1>Here is a page for editing or deleting existing INTERNATIONAL companies</h1>')
