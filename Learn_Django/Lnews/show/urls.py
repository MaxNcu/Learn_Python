from django.urls import path
from . import views
from . import index
urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('show/',views.show,name='show'),
    path('search/',views.search,name='search'),
    path('',index.index,name='index'),
    path('login_home/',index.login_index,name='login_index'),
    path('register_home/',index.register_index,name='register_index')
]