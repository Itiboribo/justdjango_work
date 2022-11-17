from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context ={
        "leads":leads
    }
        
    return render(request, "leadsapp/lead_list.html", context)

def lead_detail(request, pk):
    return HttpResponse