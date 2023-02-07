from django.http import HttpResponse
from .models import CompanyLoc, CompanyInt

def index(request):
    all_companies_loc = CompanyLoc.objects.all()
    all_companies_int = CompanyInt.objects.all()
    html = ''
    for company_loc in all_companies_loc:
        url = '/companies/detail_loc/' + str(company_loc.id) + '/'
        html += '<a href="' + url + '">' + company_loc.company_name + '</a><br>'
    for company_int in all_companies_int:
        url = '/companies/detail_int/' + str(company_int.id) + '/'
        html += '<a href="' + url + '">' + company_int.company_name + '</a><br>'

    return HttpResponse(html)


def register_loc(request):
    return HttpResponse('<h1>Here is a page for creation of new LOCAL companies</h1>')


def detail_loc(request, companyloc_id):
    return HttpResponse('<h1>Here is a page for editing or deleting of local company ' + str(companyloc_id) + '</h1>')


def register_int(request):
    return HttpResponse('<h1>Here is a page for creation of new INTERNATIONAL companies</h1>')


def detail_int(request, companyint_id):
    return HttpResponse('<h1>Here is a page for editing or deleting of international company ' + str(companyint_id) + '</h1>')
