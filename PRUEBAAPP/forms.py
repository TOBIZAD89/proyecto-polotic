from PRUEBAAPP.models import Contacto
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class FormContactoCustom(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Contacto
        fields = ('email', 'mensaje')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.TextInput(attrs={'class': 'form-control'}),
        }        



class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=150, required=True, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=30, required=True, help_text='Requerido. Al menos 8 caracteres y no pueden ser todos numeros.')
    password2 = forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=30, required=True, help_text='Requerido. Ingrese la misma contraseña que antes, para verificación.')
    first_name = forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False, help_text='Opcional.')
    last_name = forms.CharField(
        label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=254, required=True, help_text='Se requiere una direccion de email valida.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )