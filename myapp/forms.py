from django import forms
from .models import Aloqa, Stol_Buyurtma
from django.forms.widgets import Select, Widget

class AloqaForm(forms.ModelForm):
    class Meta:
        model = Aloqa
        fields = '__all__'

        widgets = {
        'ism':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ism kiriting'}),
        'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email kiriting'}),
        'xabar':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Xabar kiriting'}),
        }

class Stol_BuyurtmaForm(forms.ModelForm):
    class Meta:
        model = Stol_Buyurtma
        fields = '__all__'

        widgets = {
        'ism':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ism kiriting'}),
        'tel':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nomer kiriting'}),
        'sana':forms.SelectDateWidget(attrs={'class':'form-control'}),
        'vaqt':forms.TimeInput(attrs={'class':'form-control'}),
        'soni':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Odamlar sonini kiriting'}),
        'izoh':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh kiriting'}),
        }
