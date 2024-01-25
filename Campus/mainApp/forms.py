from django import forms
from mainApp.models import Posteo,Comentario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfesorForm(forms.Form):
    nom = forms.CharField(max_length = 30)
    dni = forms.IntegerField()
    cont=forms.CharField(max_length = 16)
    email = forms.EmailField()
    pass

class AlumnoForm(forms.Form):
    nom = forms.CharField(max_length = 30)
    dni = forms.IntegerField()
    email = forms.EmailField()
    pass

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo 
        fields = ['titulo','cuerpo']
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name= forms.CharField()
    class Meta:
        model = User 
        fields = ['email','password1','password2','last_name','first_name']
        
class AvatarForm(forms.Form):
    image = forms.ImageField()

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario 
        fields = ['contenido']
