from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.core import serializers
from django.http import JsonResponse
import json
import csv

def render_search(request):
	return render(request, 'search.html')

def purge_db(request):
      Variant.objects.all().delete()
      return JsonResponse({'Status': "Success"})

def upload_info(request):
      file_name = request.GET.get('file_name', None)
      with open(file_name, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar= '"')
            for column in spamreader:
                  _, created = Variant.objects.update_or_create(
                  gene=column[0],
                  nucleotide_change=column[1],
                  protein_change=column[2],
                  other_mappings=column[3],
                  alias=column[4],
                  transcripts=column[5],
                  region=column[6],
                  reported_classification=column[7],
                  inferred_classification=column[8],
                  source=column[9],
                  last_evaluated=column[10],
                  last_updated=column[11],
                  url=column[12],
                  submitter_comment=column[13],
                  assembly=column[14],
                  chr=column[15],
                  genomic_start=column[16],
                  genomic_stop =column[17],
                  ref=column[18],
                  alt=column[19],
                  accession=column[20],
                  reported_ref=column[21],
                  reported_alt=column[22],)
      return JsonResponse({'Status': "Success"})

def perform_search(request):
	search_by = request.GET.get('search_by', None)
	results = Variant.objects.filter(gene=search_by).values()
	results_list=list(results)
	data = {
		'results': results_list,
	}
	return JsonResponse(data)

def type_ahead(request):
      search_by = request.GET.get('search_by', None)
      results = Variant.objects.filter(gene__istartswith=search_by).values_list('gene', flat=True)
      results_list=list(set(list(results)))
      data = {
           'results': results_list,
      }
      return JsonResponse(data)
