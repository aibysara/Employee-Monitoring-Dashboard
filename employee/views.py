from django.shortcuts import render
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from employee import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from employee import models
from django.utils import timezone
from employee.models import Employee

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return redirect('userlogin')
def signup_view(request):
    return render(request, 'index.html')



def admin_signup_view(request):
    form = forms.AdminSigupForm()
    if request.method == 'POST':
        form = forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            messages.success(request, "Admin account created successfully.")
            return HttpResponseRedirect('userlogin')
        messages.error(request, "Error. Admin account creation failed.")
    return render(request, 'adminsignup.html', {'form': form})

def employee_signup_view(request):
    userForm = forms.EmployeeUserForm()
    employeeForm = forms.EmployeeForm()
    mydict = {'userForm': userForm, 'employeeForm': employeeForm}
    if request.method == 'POST':
        userForm = forms.EmployeeUserForm(request.POST)
        employeeForm = forms.EmployeeForm(request.POST, request.FILES)
        if userForm.is_valid() and employeeForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            employee = employeeForm.save(commit=False)
            employee.user = user
            employee.save()
            my_employee_group = Group.objects.get_or_create(name='EMPLOYEE')
            my_employee_group[0].user_set.add(user)
            messages.success(request, "Employee account created successfully.")
            return HttpResponseRedirect('userlogin')
        messages.error(request, "Error. Employee account creation failed.")
    return render(request, 'employeesignup.html', context=mydict)


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()



def is_employee(user):
    return user.groups.filter(name='EMPLOYEE').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')

    elif is_employee(request.user):
        accountapproval = models.Employee.objects.all().filter(user_id=request.user.id, status=True)
        x=Employee.objects.get(user_id=request.user.id,status=True)
        if accountapproval:
            a=timezone.now()
            ist_time = a.astimezone(timezone.get_current_timezone())
            print(ist_time)
            x.last_activity=ist_time
            x.save()

            #accountapproval.last_activity.save()
            return redirect('reception-dashboard')
        else:
            return render(request, 'employee_wait_for_approval.html')



@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    # for tables in admin dashboard
    employees = models.Employee.objects.all().order_by('-id')

    myDict = {

        'employees': employees,

    }
    return render(request, 'admin_dashboard.html', context=myDict)

@login_required(login_url='userlogin')
@user_passes_test(is_employee)
def reception_dashboard_view(request):
    employee = models.Employee.objects.get(user_id=request.user.id)
    return render(request, 'reception_dashboard.html',
                  context={'employee': employee})
@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def admin_employee_view(request):
    return render(request, 'admin_employee.html')

@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def admin_view_employee_view(request):
    employees = models.Employee.objects.all().filter(status=True)
    return render(request, 'admin_view_employee.html', {'employees': employees})
@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def admin_add_employee_view(request):
    userForm = forms.EmployeeUserForm()
    employeeForm = forms.EmployeeForm()
    myDict = {'userForm': userForm, 'employeeForm': employeeForm}
    if request.method == 'POST':
        userForm = forms.EmployeeUserForm(request.POST)
        employeeForm = forms.EmployeeForm(request.POST, request.FILES)
        if userForm.is_valid() and employeeForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            employee = employeeForm.save(commit=False)
            employee.user = user
            employee.status = True
            employee.save()

            my_employee_group = Group.objects.get_or_create(name='EMPLOYEE')
            my_employee_group[0].user_set.add(user)
            messages.success(request, "Employee added successfully.")
            return HttpResponseRedirect('admin-view-employee')
        messages.error(request, "Error. Registration failed.")
    return render(request, 'admin_add_employee.html', context=myDict)

@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def admin_update_employee_view(request, pk):
    employee = models.Employee.objects.get(id=pk)
    user = models.User.objects.get(id=employee.user_id)

    userForm = forms.EmployeeUserForm(instance=user)
    employeeForm = forms.EmployeeForm(instance=employee)
    myDict = {'userForm': userForm, 'employeeForm': employeeForm}
    if request.method == 'POST':
        userForm = forms.EmployeeUserForm(request.POST, instance=user)
        employeeForm = forms.EmployeeForm(request.POST,request.FILES, instance=employee)
        if userForm.is_valid() and employeeForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            employee = employeeForm.save(commit=False)
            employee.status = True
            employee.save()
            messages.success(request, "Updating successful.")
            return redirect('admin-view-employee')
        messages.error(request, "Error. Updating failed.")
    return render(request, 'admin_update_employee.html', context=myDict)

@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def admin_delete_employee_view(request, pk):
    employee = models.Employee.objects.get(id=pk)
    user = models.User.objects.get(id=employee.user_id)
    user.delete()
    employee.delete()
    return redirect('admin-view-employee')


@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def admin_approve_employee_view(request):
    employees = models.Employee.objects.all().filter(status=False)
    return render(request, 'admin_approve_employee.html', {'employees': employees})

@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def approve_employee_view(request, pk):
    employee = models.Employee.objects.get(id=pk)
    employee.status = True
    employee.save()
    return redirect(reverse('admin-approve-employee'))

@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def reject_employee_view(request, pk):
    employee = models.Employee.objects.get(id=pk)
    user = models.User.objects.get(id=employee.user_id)
    user.delete()
    employee.delete()
    return redirect('admin-approve-employee')
# Create your views here.
@login_required(login_url='userlogin')
@user_passes_test(is_admin)
def admin_view(request):
    employees = models.Employee.objects.all().filter(status=True)
    return render(request, 'employeee_status.html', {'employees': employees})