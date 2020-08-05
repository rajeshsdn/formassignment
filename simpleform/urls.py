from django.urls import path
from . import views
from . import contactform

app_name = 'simpleform'

# urlpatterns = [
#     path('mainpage', views.PAnalysisview),
#     path('contact/', contactform.contact, name='contact')
# ]

urlpatterns = [
    path('mainpage/', views.PAnalysisview),
    path("create/", views.create, name="create"),
    path("thanks/", views.showthanks),
    path("allcontacts/",views.showallcontacts),
#     path('contact/', contactform.contact, name='contact')
#    path('form', views.contactinputview),
    #    path("",views.home, name="home"),
]