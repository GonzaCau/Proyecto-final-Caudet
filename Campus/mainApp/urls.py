
from django.urls import path
from . import views
from mainApp.views import verEstudiantes,detalleEstudiante, agregarEstudiante, updateEstudiante, borrarEstudiante,login_request,registrar,editarPerfil,avatar
from mainApp.views import HacerPost, ListaPosts, EditarPost, BorrarPost , HacerComentario
#path para logout
from django.contrib.auth.views import LogoutView
#para los avatares
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #index y estaticas
    path('',views.index,name='Home'),
    path('about',views.about,name='About'),
    
    #profesor 
    path('profesor/',views.profesor,name='profesor'),
    
    #estudiante
    #path para views con class
    path('estudiante/list', verEstudiantes.as_view(), name='list'),
    path('detalleEstudiante/<pk>', detalleEstudiante.as_view(),name='Detail'),
    path('editarEstudiante/<pk>', updateEstudiante.as_view(),name='Edit'),
    path('borrarEstudiante/<pk>', borrarEstudiante.as_view(),name='Delete'),
    path('crearEstudiante/',agregarEstudiante.as_view(),name="Add"),
    
    #log in // log out // registro de usario
    path('login',login_request, name = 'Login'),
    path('registrar',registrar, name='Registrar'),
    path('logout',LogoutView.as_view(template_name = 'logout.html'), name='Logout'),
    path('editarPerfil',editarPerfil,name='EditarPerfil'),
    path('avatar',avatar,name='Avatar'),
    
    #CRUD POST
    path('postear',HacerPost.as_view(),name='Postear'),
    path('editarPost/<pk>',EditarPost.as_view(),name='EditarPost'),
    path('listaPost',ListaPosts.as_view(),name='ListaPosts'),
    path('borrarPost/<pk>',BorrarPost.as_view(),name='BorrarPost'),
    
    #CRUD COMENTS
    path('comentar',HacerComentario.as_view(),name='Comentar'),
    #path('editarComentario/<pk>',EditarComentario.as_view(),name='EditarComentario'),
    #path('verPost',VerPost.as_view(),name='VerPost'),
    #path('borrarComentario/<pk>',BorrarComentario.as_view(),name='BorrarComentario'),
]


