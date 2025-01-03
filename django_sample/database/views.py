from django.shortcuts import render
from django.http import HttpResponse
from . forms import QueryForm
from django.db.models import Q, Func, Value
from .models import Cssr, Issr, Ssr, Vntr

# Create your views here.

def home(request):
    return render(request, "database/home.html")

def query(request):
    form = QueryForm()

    if request.method == 'POST':
        form = QueryForm(request.POST)

        if form.is_valid():
            q_objects = Q()
            collected_data = form.cleaned_data

            
            
            if collected_data['type'] == 'vntr':
                if collected_data['clade']:
                    q_objects &= Q(clade__icontains = collected_data['clade'])

                if collected_data['subclade']:
                    q_objects &= Q(subclade__icontains = collected_data['subclade'])

                if collected_data['gisaid_accession']:
                    q_objects &= Q(gisaid_accession__icontains = collected_data['gisaid_accession'])
                
                
                if q_objects:
                    results = Vntr.objects.filter(q_objects)

                    queryset_data = []
                    queryset_data = list(results.values())

                    context = []

                    for item in queryset_data:
                        context.append({
                            'sequence':item['sequence'],
                            'motif':item['motif'],
                            'repeat':item['repeat'],
                            'start':item['start'],
                            'end':item['end'],
                            'length':item['length'],
                            'clade':item['clade'],
                            'subclade':item['subclade']
                        })
                    return render(request, 'database/view_vntr.html', {'context':context,
                                                                       'search_type':collected_data['type'].upper(),
                                                                       'len':len(context)})
                

                



    return render(request, "database/query.html", {'form':form})

def about(request):
    return render(request, "database/about.html")

def contact(request):
    return render(request, "database/contact.html")