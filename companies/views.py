from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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
    return render(request, 'companies/register_loc.html')


def detail_loc(request, companyloc_id):
    company_loc = get_object_or_404(CompanyLoc, pk=companyloc_id)
    return render(request, 'companies/detail_loc.html', {'company_loc': company_loc})


def register_int(request):
    return HttpResponse('<h1>Here is a page for creation of new INTERNATIONAL companies</h1>')


def detail_int(request, companyint_id):
    company_int = get_object_or_404(CompanyLoc, pk=companyint_id)
    return render(request, 'companies/detail_int.html', {'company_int': company_int})


def type_selected(request, new_loc_type):
    return render(request, 'companies/register_loc.html')