from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profesor(models.Model):
    nom = models.CharField(max_length = 30)
    dni = models.IntegerField()
    cont=models.CharField(max_length = 16)
    email = models.EmailField()
    autorizacion = True
    
class Estudiante(models.Model):
    nom = models.CharField(max_length = 30)
    dni = models.IntegerField()
    email = models.EmailField()
    autorizacion = False
    
    


class Posteo(models.Model):
    titulo = models.CharField(max_length = 100)
    creador =  models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.CharField(max_length = 512)
'''    creado = models.DateField() #en el view agregar 'creado = datetime.datetime.now' y 'creado = creado' antes de el save'''
    
class Comentario(models.Model):
    posteo = models.ForeignKey('Posteo', on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.CharField(max_length = 255)
    #posteo = models.ForeignKey(Posteo, on_delete=models.CASCADE, default = 1)
'''    creado = models.DateField() #en el view agregar 'creado = datetime.datetime.now'y 'creado = creado' antes de el save'''

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to = 'avatares' , null = True, blank = True) 
    def __str__(self):
        return f'{self.user} - {self.image}'
  