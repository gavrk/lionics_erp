from django.http import HttpResponse, FileResponse
from .models import StandardTesContract
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from companies.models import ClientLoc, OwnLoc
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Here is Doc Generator Index</h1>')


@method_decorator(csrf_exempt, name='dispatch')
class StandardTesCreate(CreateView):
    model = StandardTesContract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_clientloc'] = ClientLoc.objects.all()
        context['all_ownloc'] = OwnLoc.objects.all()

        print(OwnLoc.objects.all())

        return context

    fields = [
        'agent',
        'customer',
        'contract_number',
        'contract_date',
        'contract_city',
        'valid_until',
        'blank',
        'stamped',
    ]
    success_url = reverse_lazy('docs:index')


@method_decorator(csrf_exempt, name='dispatch')
class StandardTesUpdate(UpdateView):
    model = StandardTesContract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_clientloc'] = ClientLoc.objects.all()
        context['all_ownloc'] = OwnLoc.objects.all()

        print(OwnLoc.objects.all())

        return context

    fields = [
        'agent',
        'customer',
        'contract_number',
        'contract_date',
        'contract_city',
        'valid_until',
        'blank',
        'stamped',
    ]
    success_url = reverse_lazy('docs:index')

def stc_pdf(request, pk):
    stc = get_object_or_404(StandardTesContract, pk=pk)


    return render(request, 'companies:docs_clientloc', context)