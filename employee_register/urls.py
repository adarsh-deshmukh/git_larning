from employee_register import views
from django.urls import path

urlpatterns = [
    path('emplist', views.employee_list, name='emplist'),  
    path('empform', views.employee_form, name='empform'), 
    path('empupdate/<int:x>',views.employee_update,name="empupdate"),
    #path('empdelete', views.employee_delete, name='empdelete'), 
]