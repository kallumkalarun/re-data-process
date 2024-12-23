from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('gdc-sd-api-in/', views.gdcsdapiin_view, name="gdc-sd-api-in"),
    path('gdc-sd-api-out/', views.gdcsdapiout_files, name='gdc-sd-api-out'),

]
