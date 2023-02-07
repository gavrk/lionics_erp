from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import CompanyLoc, CompanyInt

def index(request):
    all_companies_loc = CompanyLoc.objects.all()
    all_companies_int = CompanyInt.objects.all()
    context = {
        'all_companies_loc': all_companies_loc,
        'all_companies_int': all_companies_int,
    }

    return render(request, 'companies/index.html', context)


def register_loc(request):
    return HttpResponse('<h1>Here is a page for creation of new LOCAL companies</h1>')


def detail_loc(request, companyloc_id):
    try:
        company_loc = CompanyLoc.objects.get(pk=companyloc_id)
    except CompanyLoc.DoesNotExist:
        raise Http404('Local company does not exist')
    return render(request, 'companies/detail_loc.html', {'company_loc': company_loc})


def register_int(request):
    return HttpResponse('<h1>Here is a page for creation of new INTERNATIONAL companies</h1>')


def detail_int(request, companyint_id):
    try:
        company_int = CompanyInt.objects.get(pk=companyint_id)
    except CompanyInt.DoesNotExist:
        raise Http404('International company does not exist')
    return render(request, 'companies/detail_int.html', {'company_int': company_int})