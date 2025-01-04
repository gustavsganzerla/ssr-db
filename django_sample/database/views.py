from django.shortcuts import render
from django.http import HttpResponse
from . forms import QueryForm
from django.db.models import Q, Func, Value
from .models import Cssr, Issr, Ssr, Vntr
import csv

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

                    request.session['context'] = context    
                    return render(request, 'database/view_vntr.html', {'context':context,
                                                                       'search_type':collected_data['type'].upper(),
                                                                       'len':len(context)})
                
            if collected_data['type'] == 'cssr':
                if collected_data['clade']:
                    q_objects &= Q(clade__icontains = collected_data['clade'])

                if collected_data['subclade']:
                    q_objects &= Q(subclade__icontains = collected_data['subclade'])

                if collected_data['gisaid_accession']:
                    q_objects &= Q(gisaid_accession__icontains = collected_data['gisaid_accession'])

                if q_objects:
                    results = Cssr.objects.filter(q_objects)
                    
                    queryset_data = []
                    queryset_data = list(results.values())

                    context = []

                    for item in queryset_data:
                        context.append({
                            'sequence':item['sequence'],
                            'start':item['start'],
                            'end':item['end'],
                            'motif':item['motif'],
                            'complexity':item['complexity'],
                            'length':item['length'],
                            'gap':item['gap'],
                            'component':item['component'],
                            'structure':item['structure'],
                            'clade':item['clade'],
                            'subclade':item['subclade']
                            })
                    request.session['context'] = context    
                    return render(request, 'database/view_cssr.html', {'context':context,
                                                                       'search_type':collected_data['type'].upper(),
                                                                       'len':len(context)})
                    

    return render(request, "database/query.html", {'form':form})

def about(request):
    return render(request, "database/about.html")

def contact(request):
    return render(request, "database/contact.html")


def download_vntr(request):
    context = request.session.get('context', None)
    
    if context:
        csv_content = []
        csv_content.append(['sequence', 'motif', 'repeat', 'start', 'end', 'length', 'clade', 'subclade'])

        for entry in context:
            csv_content.append([
                entry['sequence'],
                entry['motif'],
                entry['repeat'],
                entry['start'],
                entry['end'],
                entry['length'],
                entry['clade'],
                entry['subclade']
            ])

        if csv_content:
            response = HttpResponse(content_type = "text/csv")
            response['Content-Disposition'] = 'attachment; filename = "result_vntr.csv"'

            csv_writer = csv.writer(response)

            for row in csv_content:
                csv_writer.writerow(row)
            return response
        
def download_cssr(request):
    context = request.session.get('context', None)
    
    if context:
        csv_content = []
        csv_content.append(['sequence', 'start', 'end', 'motif', 'complexity', 'length', 'gap', 'component', 'structure', 'clade', 'subclade'])

        for entry in context:
            csv_content.append([
                entry['sequence'],
                entry['start'],
                entry['end'],
                entry['motif'],
                entry['complexity'],
                entry['length'],
                entry['gap'],
                entry['component'],
                entry['structure'],
                entry['clade'],
                entry['subclade']
            ])

        if csv_content:
            response = HttpResponse(content_type = "text/csv")
            response['Content-Disposition'] = 'attachment; filename = "result_cssr.csv"'

            csv_writer = csv.writer(response)

            for row in csv_content:
                csv_writer.writerow(row)
            return response