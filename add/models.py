from django.db import models



class Employee(models.Model):
    Emp_Name = models.CharField(max_length=80)
    Emp_Address = models.CharField(max_length=150)
    class Meta:
        unique_together = (("Emp_Name", "Emp_Address"))


class TaxInfo2(models.Model):
    Tax_Name = models.CharField(max_length=25, unique = True)


class Expenses2(models.Model):
    Date = models.DateField(null=True)
    Category = models.CharField(max_length=100)
    Emp_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Expense_Desc = models.CharField(max_length=100)
    Tax_ID = models.ForeignKey(TaxInfo2, on_delete=models.CASCADE)
    Pre_Tax_amt = models.FloatField(null=True)
    Tax_Amt = models.FloatField(null=True)


