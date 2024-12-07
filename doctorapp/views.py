from django.shortcuts import render

# Create your views here.
def Homepage(request):
    return render(request, 'doctorapp/Homepage.html')

def Success(request):
    return render(request, 'doctorapp/Success.html')


from django.shortcuts import render
from .models import Appointment


def display_appointments(request):
    # Retrieve all appointments from the database
    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments
    }
    return render(request, 'userapp/display_appointments.html', context)

