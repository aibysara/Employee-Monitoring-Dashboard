"""
URL configuration for Employee_Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from employee import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('userlogin', LoginView.as_view(template_name='userlogin.html', redirect_authenticated_user=True),
         name='userlogin'),
    path('logout', LogoutView.as_view(template_name='userlogin.html'), name='logout'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('signup', views.signup_view, name='signup'),

    path('adminsignup', views.admin_signup_view, name='adminsignup'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-employee', views.admin_employee_view, name='admin-employee'),
    path('admin-approve-employee', views.admin_approve_employee_view, name='admin-approve-employee'),
    path('approve-employee/<int:pk>', views.approve_employee_view, name='approve-employee'),
    path('reject-employee/<int:pk>', views.reject_employee_view, name='reject-employee'),
    path('admin-view-employee', views.admin_view_employee_view, name='admin-view-employee'),
    path('admin-add-employee', views.admin_add_employee_view, name='admin-add-employee'),
    path('admin-delete-employee/<int:pk>', views.admin_delete_employee_view, name='admin-delete-employee'),
    path('admin-update-employee/<int:pk>', views.admin_update_employee_view, name='admin-update-employee'),
    path('employeesignup', views.employee_signup_view, name='employeesignup'),
    path('admin-view', views.admin_view, name='admin-view'),
    path('reception-dashboard', views.reception_dashboard_view, name='reception-dashboard'),
]
if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
