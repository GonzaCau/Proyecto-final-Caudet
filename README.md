# Proyecto final Caudet
 Proyecto final del curso Programacion con Django 

*superuser:
username = Admin01
password = ihatemahito

*usuarios de prueba:
username = testUser
password = randomuser001

username = registerTest01
username = 123456asdasd789

DESCRIPCION
El proposito de este proyecto fue, en un principio, hacer un campus para
alguna entidad  educativa, a medida que el proyecto fue avanzando, me di
cuenta que probablemente seria algo muy ambicioso de hacer, lo que me llevo
a condensar el proyecto a funciones escenciales.

USAR EL PROYECTO
Para usar el proyecto hay que correr el servidor por la consola de comandos,
nos situamos a la altura de 'manage.py' y ejecutamos el comando:
    python manage.py runserver
en el navegador nos dirigimos al puerto local que tengas configurado.

ESTRUCTURA
El proyecto tiene 4 carpetas:
-Campus = dentro esta la carpeta 'plantillas', que contiene todos los html.
-mainApp = esta es la APP principal, dentro tenemos models.py , forms.py , urls.py , views.py
-media = contiene las imagenes usadas en el proyecto, tambien la carpeta avatares (funcion a implementar)
-static = contiene los statics de la plantilla principal (index.html)
la DB de sqlite3 y el manage.py

ESTADO DEL PROYECTO
El proyecto esta ciertamente incompleto, solo cubre lo basico:
-log in
-log out
-CRUD para posts
-CRUD para alumnos (requiere retoques, si se quiere acceder hay que hacerlo con "/estudiante/list")
-About page

Pese a esto , creo que tiene una buena base para, o bien completarlo y que funcione como un campus
o bien usarlo como base para un blog o un foro.

  *NOTA*
*para ingresar a la ventana del admin, hay que ir a la url y agregar " /admin ".
*la funcion para agreagr un Avatar todavia no esta terminada.
