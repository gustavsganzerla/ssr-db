from django.shortcuts import render
from django.http import HttpResponse
from . forms import QueryForm
from django.db.models import Q, Func, Value
from .models import Cssr, Issr, Ssr, Vntr, Ssr_primers
import csv
from django.db.models.functions import Length

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
                    q_objects &= Q(sequence__icontains = collected_data['gisaid_accession'])
                
                
                if q_objects:
                    results = Vntr.objects.filter(q_objects)

                    queryset_data = []
                    queryset_data = list(results.values())

                    context = []

                    for item in queryset_data:
                        if collected_data['length'] == 'h6':
                            if int(len(item['motif'])) > 6:
                                context.append({
                                        'id':item['id'],
                                        'sequence':item['sequence'],
                                        'motif':item['motif'],
                                        'repeat':item['repeat'],
                                        'start':item['start'],
                                        'end':item['end'],
                                        'length':item['length'],
                                        'clade':item['clade'],
                                        'subclade':item['subclade']
                                    })
                        else:
                            if int(collected_data['length']) == int(len(item['motif'])):
                                context.append({
                                        'id':item['id'],
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
                
            if collected_data['type'] == 'cssr':
                if collected_data['clade']:
                    q_objects &= Q(clade__icontains = collected_data['clade'])

                if collected_data['subclade']:
                    q_objects &= Q(subclade__icontains = collected_data['subclade'])

                if collected_data['gisaid_accession']:
                    q_objects &= Q(sequence__icontains = collected_data['gisaid_accession'])

                if q_objects:
                    results = Cssr.objects.filter(q_objects)
                    
                    queryset_data = []
                    queryset_data = list(results.values())

                    context = []

                    for item in queryset_data:
                        motif = item['motif']
                        aux = motif.split('-')
                        
                        if collected_data['length'] == 'h6':
                                if int(len(aux[0])) > 6:
                                    context.append({
                                        'id':item['id'],
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
                        else:
                            if int(collected_data['length']) == int(len(aux[0])):
                                context.append({
                                        'id':item['id'],
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
                    return render(request, 'database/view_cssr.html', {'context':context,
                                                                       'search_type':collected_data['type'].upper(),
                                                                       'len':len(context)})
                    
            if collected_data['type'] == 'issr':
                if collected_data['clade']:
                    q_objects &= Q(clade__icontains = collected_data['clade'])

                if collected_data['subclade']:
                    q_objects &= Q(subclade__icontains = collected_data['subclade'])

                if collected_data['gisaid_accession']:
                    q_objects &= Q(sequence__icontains = collected_data['gisaid_accession'])



                if q_objects:
                    results = Issr.objects.filter(q_objects)
                    
                    queryset_data = []
                    queryset_data = list(results.values())

                    context = []

                    for item in queryset_data:
                        if collected_data['length'] == 'h6':
                                if int(len(item['motif'])) > 6:
                                    context.append({
                                        'id':item['id'],
                                        'sequence':item['sequence'],
                                        'standard':item['standard'],
                                        'motif':item['motif'],
                                        'start':item['start'],
                                        'end':item['end'],
                                        'length':item['length'],
                                        'match':item['match'],
                                        'subsitution':item['subsitution'],
                                        'insertion':item['insertion'],
                                        'deletion':item['deletion'],
                                        'score':item['score'],
                                        'clade':item['clade'],
                                        'subclade':item['subclade']
                                    })
                        else:
                            if int(collected_data['length']) == int(len(item['motif'])):
                                context.append({
                                            'id':item['id'],
                                            'sequence':item['sequence'],
                                            'standard':item['standard'],
                                            'motif':item['motif'],
                                            'start':item['start'],
                                            'end':item['end'],
                                            'length':item['length'],
                                            'match':item['match'],
                                            'subsitution':item['subsitution'],
                                            'insertion':item['insertion'],
                                            'deletion':item['deletion'],
                                            'score':item['score'],
                                            'clade':item['clade'],
                                            'subclade':item['subclade']
                                        })   
                    return render(request, 'database/view_issr.html', {'context':context,
                                                                       'search_type':collected_data['type'].upper(),
                                                                       'len':len(context)})

            if collected_data['type'] == 'ssr':
                if collected_data['clade']:
                    q_objects &= Q(clade__icontains = collected_data['clade'])

                if collected_data['subclade']:
                    q_objects &= Q(subclade__icontains = collected_data['subclade'])

                if collected_data['gisaid_accession']:
                    q_objects &= Q(sequence__icontains = collected_data['gisaid_accession'])
                

                if q_objects:
                    results = Ssr.objects.filter(q_objects)
                    
                    queryset_data = []
                    queryset_data = list(results.values())

                    context = []

                    for item in queryset_data:
                            if collected_data['length'] == 'h6':
                                if int(len(item['motif'])) > 6:
                                    context.append({
                                    'id':item['id'],
                                    'sequence':item['sequence'],
                                    'standard':item['standard'],
                                    'motif':item['motif'],
                                    'repeat':item['repeat'],
                                    'start':item['start'],
                                    'end':item['end'],
                                    'length':item['length'],
                                    'clade':item['clade'],
                                    'subclade':item['subclade']
                                })
                            else:
                                if int(collected_data['length']) == int(len(item['motif'])):
                                 context.append({
                                    'id':item['id'],
                                    'sequence':item['sequence'],
                                    'standard':item['standard'],
                                    'motif':item['motif'],
                                    'repeat':item['repeat'],
                                    'start':item['start'],
                                    'end':item['end'],
                                    'length':item['length'],
                                    'clade':item['clade'],
                                    'subclade':item['subclade']
                                })
                    return render(request, 'database/view_ssr.html', {'context':context,
                                                                       'search_type':collected_data['type'].upper(),
                                                                       'len':len(context),
                                                                       'clade':collected_data['clade'],
                                                                       'subclade':collected_data['subclade'],
                                                                       'length':collected_data['length']})




    return render(request, "database/query.html", {'form':form})


def statistics(request):
    return render(request, "database/statistics.html")

def faq(request):
    return render(request, "database/faq.html")

def about(request):
    return render(request, "database/about.html")

def contact(request):
    return render(request, "database/contact.html")


###downloads
def download_vntr(request):
     if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
        
        items = Vntr.objects.filter(id__in=selected_ids)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=vntr_results.csv'

        writer = csv.writer(response)

        writer.writerow(['Sequence', 'Motif', 'Repeat', 'Start',
                          'End', 'Length', 'Clade', 'Subclade'])  

        
        for item in items:
            writer.writerow([
                item.sequence, item.motif, item.repeat, item.start, item.end, 
                item.length, item.clade, item.subclade
            ])
        
        return response
        
def download_cssr(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
        
        items = Cssr.objects.filter(id__in=selected_ids)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=cssr_results.csv'

        writer = csv.writer(response)

        writer.writerow(['Sequence', 'Start', 'End', 'Motif', 'Complexity', 'Length', 
                         'Gap', 'Component', 'Structure', 'Clade', 'Subclade'])  

        
        for item in items:
            writer.writerow([
                item.sequence, item.start, item.end, item.motif, 
                item.complexity, item.length, item.gap, item.component, 
                item.structure, item.clade, item.subclade
            ])
        
        return response

def download_issr(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
        
        items = Issr.objects.filter(id__in=selected_ids)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=issr_results.csv'

        writer = csv.writer(response)

        writer.writerow(['Sequence', 'Standard', 'Motif', 'Start',
                          'End', 'Length', 'Match', 'Substitution', 'Insertion', 
                         'Deletion', 'Score', 'Clade', 'Subclade'])  

        
        for item in items:
            writer.writerow([
                item.sequence, item.standard, item.motif, item.start, item.end, 
                item.length, item.match, item.subsitution, item.insertion, item.deletion,
                item.score, item.clade, item.subclade
            ])
        
        return response
        
def download_ssr(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
        
        items = Ssr.objects.filter(id__in=selected_ids)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=ssr_results.csv'

        writer = csv.writer(response)

        writer.writerow(['Sequence', 'Standard', 'Motif', 'Repeat', 'Start',
                          'End', 'Length', 'Clade', 'Subclade'])  

        
        for item in items:
            writer.writerow([
                item.sequence, item.standard, item.motif, item.repeat, item.start, item.end, 
                item.length, item.clade, item.subclade
            ])
        
        return response
    

def view_primers(request):
    if request.method == 'POST':
        clade = request.POST.get('clade')
        subclade = request.POST.get('subclade')
        length = request.POST.get('length')

        

        q_objects = Q()
        q_objects &= Q(clade__icontains = clade)
        q_objects &= Q(subclade__icontains = subclade)

        if q_objects:
                    results = Ssr_primers.objects.filter(q_objects)
                    
                    queryset_data = []
                    queryset_data = list(results.values())

                    context = []
                    #id	sequence	standard	motif	{type}	repeat	start	end	length	
                    #product	forward	tm_forward	gc_forward	stability_forward	reverse	tm_reverse	gc_reverse	stability_reverse	clade	subclade
                    for item in queryset_data:
                        if int(length) == int(len(item['motif'])):
                            context.append({
                                'id':item['id'],
                                'sequence':item['sequence'],
                                'standard':item['standard'],
                                'motif':item['motif'],
                                'repeat':item['repeat'],
                                'start':item['start'],
                                'end':item['end'],
                                'length':item['length'],
                                'product':item['product'],
                                'forward':item['forward'],
                                'tm_forward':item['tm_forward'],
                                'gc_forward':item['gc_forward'],
                                'stability_forward':item['stability_forward'],
                                'reverse':item['reverse'],
                                'tm_reverse':item['tm_reverse'],
                                'gc_reverse':item['gc_reverse'],
                                'stability_reverse':item['stability_reverse'],
                                'clade':item['clade'],
                                'subclade':item['subclade']
                            })
                    
                    return render(request, 'database/view_primers.html', {'context':context,
                                                                          'len':len(context)})


def download_primers(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
        
        items = Ssr_primers.objects.filter(id__in=selected_ids)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=ssr_primers_results.csv'

        writer = csv.writer(response)

        writer.writerow(['Sequence', 'Standard', 'Motif', 'Repeat', 'Start',
                          'End', 'Length', 
                          'Product', 
                          'Forward', 'Forward tm', 'Forward GC', 'Forward Stability',
                          'Reverse', 'Reverse tm', 'Reverse GC', 'Reverse Stability',
                          
                          'Clade', 'Subclade'])  

        
        for item in items:
            writer.writerow([
                item.sequence, item.standard, item.motif, item.repeat, item.start, item.end, item.length,
                item.product,
                item.forward, item.tm_forward, item.gc_forward, item.stability_forward,
                item.reverse, item.tm_reverse, item.gc_reverse, item.stability_reverse,
                item.clade, item.subclade
            ])
        
        return response