from django.urls import path
from feed import views

urlpatterns=[
    path('',views.func,name='feedpage')
]