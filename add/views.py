from django.shortcuts import render, render_to_response

# Create your views here.


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .form import UploadFileForm
from django.views.generic import View, ListView

# Imaginary function to handle an uploaded file.
from .helper import handle_uploaded_file, validate_csv
from .models import Expenses2

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = request.FILES['file']
            validate_csv(file_name)
            handle_uploaded_file(request)
    else:
        form = UploadFileForm()
    return HttpResponseRedirect("/result/")

def home(request):
    return render(request, 'add.html')

def result(request):
    import sqlite3
    try:
     db = sqlite3.connect('db.sqlite3')
     cursor = db.cursor()
     cursor.execute("select strftime('%m',Date) as Month, sum(Pre_Tax_amt) as Total from add_expenses2 group by strftime('%m',Date)")
     rows = str(cursor.fetchall())
    finally:
     db.close()

     return render_to_response('result.html', {'rows': rows})


