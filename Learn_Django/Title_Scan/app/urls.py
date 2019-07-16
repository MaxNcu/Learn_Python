from django.urls import path
from .home import home
from .login import login
from .register import register
from .register import home as reg_home
from .login import home as log_home
from .addtask import Add_Task,Del_Task
from .show import show
urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('reg_home/',reg_home,name='reg_home'),
    path('login/',login,name='login'),
    path('log_home/',log_home,name='log_home'),
    path('add_tasks/',Add_Task,name='add_tasks'),
    path('del_tasks/',Del_Task,name='del_tasks'),
    path('show/',show,name='show')
]