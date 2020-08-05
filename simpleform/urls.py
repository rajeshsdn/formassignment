from django.urls import path
from . import views

app_name = 'simpleform'

urlpatterns = [
    path('mainpage', views.PAnalysisview),

]