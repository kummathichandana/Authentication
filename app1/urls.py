from django.urls import path
from app1 import views

urlpatterns=[
    path('info',views.func2,name='ice'),
]