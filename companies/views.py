from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import CompanyLoc, CompanyInt
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def register_loc(request):
    return render(request, 'companies/register_loc.html')

def index_loc(request):
    all_companies_loc = CompanyLoc.objects.all()
    context = {
        'all_companies_loc': all_companies_loc,
    }

    return render(request, 'companies/index_loc.html', context)


def index_int(request):
    all_companies_int = CompanyInt.objects.all()
    context = {
        'all_companies_int': all_companies_int,
    }

    return render(request, 'companies/index_int.html', context)


def register_int(request):
    return HttpResponse('<h1>Here is a page for creation of new INTERNATIONAL companies</h1>')


def detail_int(request, companyint_id):
    company_int = get_object_or_404(CompanyLoc, pk=companyint_id)
    return render(request, 'companies/detail_int.html', {'company_int': company_int})

@method_decorator(csrf_exempt, name='dispatch')
class CompanyLocCreate(CreateView):
    model = CompanyLoc
    fields = ['company_type', 'company_name', 'pos_per_acc', 'position_nom', 'person_nom', 'acting_on',
              'passport_series', 'passport_number', 'pass_issued_by', 'pass_issued_date', 'pass_issued_code',
              'legal_addr', 'registration_addr', 'postal_addr', 'tel', 'email', 'bank_name', 'bic', 'curr_acc', 'corr_acc',
              'inn', 'kpp', 'ogrn', 'okpo']
    success_url = reverse_lazy('companies:index_loc')

@method_decorator(csrf_exempt, name='dispatch')
class CompanyLocUpdate(UpdateView):
    model = CompanyLoc
    fields = ['company_type', 'company_name', 'pos_per_acc', 'position_nom', 'person_nom', 'acting_on',
              'passport_series', 'passport_number', 'pass_issued_by', 'pass_issued_date', 'pass_issued_code',
              'legal_addr', 'registration_addr', 'postal_addr', 'tel', 'email', 'bank_name', 'bic', 'curr_acc',
              'corr_acc', 'inn', 'kpp', 'ogrn', 'okpo']

@method_decorator(csrf_exempt, name='dispatch')
class CompanyLocDelete(DeleteView):
    model = CompanyLoc
    success_url = reverse_lazy('companies:index_loc')
