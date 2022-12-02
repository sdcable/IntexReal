from django import forms
from .models import client
from .models import serum_entry

class Meta:
        model = client
        fields = ('first_name', 'last_name', 'email', 'password', 'dateOfBirth', 'gender', 'race')

 
class serumEntryVizForm(forms.ModelForm): # for Serum Vizualization - Megan
    class Meta:
        model = serum_entry
        fields = '__all__' #('serum_potassium',)
        labels = {
            "serum_date": "Date (mm/dd/yyyy)",
            "serum_potassium": "Potassium",
            "serum_phosphorus": "Phosphorus",
            "serum_sodium": "Sodium",
            "serum_creat": "Creatinine",
            "serum_alb": "Albumin",
            "serum_blood_sugar": "A1C (Blood Sugar)"
        }
        value = {
            "serum_date": '01/01/2000'
        }