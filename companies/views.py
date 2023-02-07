from django.http import HttpResponse
from django.template import loader
from .models import CompanyLoc, CompanyInt

def index(request):
    all_companies_loc = CompanyLoc.objects.all()
    all_companies_int = CompanyInt.objects.all()
    template = loader.get_template('companies/index.html')
    context = {
        'all_companies_loc': all_companies_loc,
        'all_companies_int': all_companies_int,
    }

    return HttpResponse(template.render(context, request))


def register_loc(request):
    return HttpResponse('<h1>Here is a page for creation of new LOCAL companies</h1>')


def detail_loc(request, companyloc_id):
    return HttpResponse('<h1>Here is a page for editing or deleting of local company ' + str(companyloc_id) + '</h1>')


def register_int(request):
    return HttpResponse('<h1>Here is a page for creation of new INTERNATIONAL companies</h1>')


def detail_int(request, companyint_id):
    return HttpResponse('<h1>Here is a page for editing or deleting of international company ' + str(companyint_id) + '</h1>')
