from django.shortcuts import render
from django.http import HttpResponse
from .models import Report

# Create your views here.
def index(request):
    reports =   Report.objects.all()
    context =   {'reports': reports}

    return render(request, 'home.html', context)

def report(request, pk):
    memo = Report.objects.get(id=pk)

    context =   {'memo': memo}

    return render(request, 'report.html', context)