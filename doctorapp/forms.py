from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['username', 'date', 'first_name', 'symptoms']
        widgets = {
            'date': forms.SelectDateWidget(years=range(2024, 2031)),  # Adjust years as needed
        }
