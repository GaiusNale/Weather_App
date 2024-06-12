from django import forms 

class WeatherForm(forms.Form):
    city = forms.CharField(max_length= 100, label= "Enter a city")