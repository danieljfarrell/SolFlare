import csv
from django.http import HttpResponse
from django.shortcuts import render
from .forms import inputParameters
from .models import plotter


graphobj=plotter()
def inputparams(request):
    global graphobj

    if 'calculate' in request.POST:
        form = inputParameters(request.POST)
        if form.is_valid():
            arc_thickness = form.cleaned_data['arc_thickness']
            texture_height = form.cleaned_data['texture_height']
            graphobj.setvalues(arc_thickness, texture_height)
            return render(request, 'index.html', {'form':form,'graph':graphobj.getgraph()})

    if 'download' in request.POST:
        # code based on https://docs.djangoproject.com/en/5.0/howto/outputting-csv/
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
        )
        writer = csv.writer(response)
        graphobj.getcsv(writer)
        return response

    form=inputParameters()
    return render(request, 'index.html', {'form':form,'graph':0})


