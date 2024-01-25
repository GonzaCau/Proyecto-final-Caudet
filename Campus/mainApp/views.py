from django.shortcuts import render
from django.http import HttpResponse

from mainApp.forms import UserEditForm, AvatarForm

#importando para las views con class
from mainApp.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#imports para log in / log out
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.models import User
#imports para Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mainApp.forms import PosteoForm , UserEditForm , ComentarioForm
from django.contrib.auth.decorators import login_required


def index(request):
    
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')
#profesor
def profesor(request):
    
    return render(request,'profesor.html')

#estudiante


#vistas con class
#profesor
  
class verEstudiantes(ListView):
    model = Estudiante
    template_name = 'listaEstudiantes.html'
   
class detalleEstudiante(DetailView):
    model = Estudiante
    template_name = 'detalleEstudiante.html'
 
class agregarEstudiante(CreateView):
    model = Estudiante
    fields = ['nom','dni','email']
    template_name = 'crearEstudiante.html'
    success_url = '/estudiante/list'
  
class updateEstudiante(UpdateView):
    model = Estudiante
    fields = ['nom','dni','email']
    template_name = 'crearEstudiante.html'
    success_url = '/estudiante/list'
 
class borrarEstudiante(DeleteView):
    model = Estudiante
    template_name = 'confirmarBorrarEstudiante.html'
    success_url = '/estudiante/list'


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'mensaje': f'Login exitoso, hola {username}'})
            else:
                return render(request, 'index.html', {'mensaje': f'Algo salio mal :( -- usuario o password incorrectos'}) #si se equivoca con usuario o password
        else:
            return render(request, 'index.html',{'mensaje':f'Algo salio mal :( -- Datos incorrectos)'}) #si los datos no son correctos
                
    
    form = AuthenticationForm()
    
    return render(request, 'login.html',{'form':form})

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'index.html',{'mensaje': f'Usuario creado'})
    
    form = UserCreationForm()
    return render(request,'registrar.html', {'form':form})

class ListaPosts(LoginRequiredMixin, ListView):
    model = Posteo
    template_name = 'post_lista.html'
    context_object_name = 'posteos'

class HacerPost(LoginRequiredMixin, CreateView):
    model = Posteo
    form_class = PosteoForm
    template_name = 'postear.html'
    success_url = reverse_lazy('ListaPosts')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class EditarPost(LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = PosteoForm
    template_name = 'post_editar.html'
    success_url = reverse_lazy('ListaPosts')

class BorrarPost(LoginRequiredMixin, DeleteView):
    model = Posteo
    template_name = 'post_borrar.html'
    success_url = reverse_lazy('ListaPosts')

class HacerComentario(LoginRequiredMixin,CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentar.html'
    success_url= reverse_lazy('ListaPosts')
    def from_valid(self,form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

    

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method =='POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            usuario.email = info.get('email')
            usuario.password1 = info.get('password1')
            usuario.password2 = info.get('password2')
            usuario.last_name = info.get('last_name')
            usuario.first_name = info.get('first_name')
            usuario.save()
            return render(request,'index.html')
    else:
        miFormulario = UserEditForm(initial= {'email':usuario.email})
        return render(request,'editarUsuario.html',{'formulario':miFormulario,'usuario':usuario})

@login_required
def avatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid(): 
            user = User.objects.get(username=request.user)
            avatar = Avatar(user=user , image=formulario.cleaned_data.get['image'])
            avatar.save()
            return render(request, 'index.html')
    else:
        formulario = AvatarForm()
    return render(request, 'avatar.html',{'formulario':formulario})

@login_required
def mostrarAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'index.html', {'url':avatares[0].image.url})

