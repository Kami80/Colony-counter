
from django.urls import path
from primer_app import views

urlpatterns = [
    path('', views.design_primer, name='design_primer'),
]
