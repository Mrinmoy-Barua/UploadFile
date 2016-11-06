import csv
from django.core.exceptions import ValidationError
from add.models import Employee, Expenses2, TaxInfo2
from io import TextIOWrapper, StringIO
import datetime

def validate_csv(value):
    if not value.name.endswith('.csv'):
        raise ValidationError('Invalid file type')

def handle_uploaded_file(request):
          csvf = StringIO(request.FILES['file'].read().decode())
          reader = csv.reader(csvf, delimiter=',')
          reader.__next__();
          for row in reader:
                save_on_employee(row[2], row[3])
                save_on_tax_info(row[6])
                save_on_expenses(row)


def save_on_employee(name, address):
    if not Employee.objects.filter(Emp_Name=name, Emp_Address=address).exists():
        em = Employee()
        em.Emp_Name = name
        em.Emp_Address = address
        em.save()


def save_on_tax_info(tax_name):
    if not TaxInfo2.objects.filter(Tax_Name=tax_name).exists():
     tx = TaxInfo2()
     tx.Tax_Name = tax_name
     tx.save()

def save_on_expenses(row):
    exp = Expenses2()
    exp.Date = datetime.datetime.strptime(row[0],'%m/%d/%Y').strftime('%Y-%m-%d')#row[0]
    exp.Category = row[1]
    exp.Emp_ID_id = Employee.objects.get(Emp_Name=row[2], Emp_Address=row[3]).id
    exp.Expense_Desc = row[4]
    exp.Pre_Tax_amt = float(row[5].replace(',',''))
    exp.Tax_ID_id = TaxInfo2.objects.get(Tax_Name=row[6]).id
    exp.Tax_Amt = float(row[7].replace(',',''))
    exp.save()

