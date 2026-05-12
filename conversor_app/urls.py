from django.urls import path
from . import views

app_name = 'conversor_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('csv-a-excel/', views.csv_to_excel_view, name='csv_to_excel'),
    path('pdf-a-word/', views.pdf_to_word_view, name='pdf_to_word'),
]