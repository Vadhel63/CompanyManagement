from django.shortcuts import render,redirect
from django.http import HttpResponse
from HR_manger.models import *
from django.http import JsonResponse
from HR_manger.models import Employee
from datetime import time

def delete_employee(request,e_id):
    if request.method == 'POST':
        employee = Employee.objects.get(id=e_id)
        employee.delete()
            
    return redirect('employeedisplay')
def update_employee(request,e_id):
    employee = Employee.objects.get(id=e_id)
    if request.method == 'POST':
        date=request.POST['date']
        e_name=request.POST['name']
        c_no=request.POST['number']
        adhar_no=request.POST['aadhar']
        location=request.POST['location']
        j_position=request.POST['position']
        gender=request.POST['gender']
        employee.name=e_name
        employee.date_of_joining=date
        employee.phone_number=c_no
        employee.aadhar_no=adhar_no
        employee.location=location
        employee.position=j_position
        employee.gender=gender
        employee.save()
        return redirect('employeedisplay')  
    else:    
        return render(request,'employeeupdate.html',{
        'employee':employee
        })
# Create your views here.
def employee(request):
    return render(request,"employee.html")
def employee1(request):
    date=request.POST['date']
    e_name=request.POST['name']
    c_no=request.POST['number']
    adhar_no=request.POST['aadhar']
    location=request.POST['location']
    j_position=request.POST['position']
    gender=request.POST['gender']
    salary=request.POST['salary']
    e=Employee.objects.create(name=e_name,phone_number=c_no,aadhar_no=adhar_no,location=location,salary=salary,gender=gender,date_of_joining=date,position=j_position)
    e.save()
    return redirect('employeedisplay')

def employeedisplay(request):
    e=Employee.objects.all()
    return render(request,'employeedisplay.html',{
        'employees':e
    })
def employeework(request):
    employee=Employee.objects.all()
    return render(request,"employeework.html",{
        'employee':employee
    })
def employeework1(request):
    date=request.POST['date']
    # get the times
    s=time.fromisoformat(request.POST['start_time'])
    f=time.fromisoformat(request.POST['end_time'])
    e=request.POST['employee']
    e1=Employee.objects.get(id=e)
    # create salary
    print(s)
    print(f)
    # print(f-s)
    # e_s = Emp_Salary(employee=e1, hourly_rate=e1.salary, total_hours_worked=(f-s) , total_salary=(e-s)*e1.salary)
    e1=Emp_WorkHour(date=date,start_time=s,end_time=f,employee=e1)
    e1.save()
    # e_s.save()
    return HttpResponse("success fully done!")

def employeesalary(request):
    return render(request,"employeesalary.html")
