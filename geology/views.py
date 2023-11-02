from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm
from django.contrib import messages

# Create your views here.
def index(request):
    reports =   Report.objects.all()
    context =   {'reports': reports}

    return render(request, 'home.html', context)

def report(request, pk):
    memo = Report.objects.get(id=pk)

    context =   {'memo': memo}

    return render(request, 'report.html', context)

def repo_form(request):
    if request.method == 'POST':
        form  =   ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your report was successfully added!'))
        else:
            message.error(request, 'Error saving form')
        
        return redirect("home")
    form = ReportForm()
    report = Report.objects.all()

    context={'form': form, 'report': report}
    return render(request,'repoform.html', context)
