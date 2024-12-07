from django.urls import path, include

from . import views
app_name='doctorapp'
urlpatterns = [
    path('Homepage/',views.Homepage,name='Homepage'),
    path('Success/',views.Success,name="Success"),
    path('display_appointments/',views.display_appointments,name="display_appointments"),

]