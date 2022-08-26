from django.urls import path
from . import views 

urlpatterns = [
    path("eng/",views.ver_cv,name="vercv"),
    path("",views.ver_cvesp,name="vercvesp"),
    path("Contacto/",views.Consultas.as_view(),name="consultas"),
    path("Contact/",views.contact.as_view(),name="questions"),
    
]