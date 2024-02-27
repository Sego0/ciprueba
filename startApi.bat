@echo off
rem Activar el entorno virtual
call C:\Users\Diego Segovia\Desktop\codes\Proyectos\CImanage2.0\venv\Scripts\activate.bat

rem Ejecutar el servidor Django
echo Iniciando servidor Django...
cd C:\Users\Diego Segovia\Desktop\codes\Proyectos\CImanage2.0
py manage.py runserver

rem Esperar unos segundos para que el servidor Django inicie completamente...
timeout /t 5

rem Desactivar el entorno virtual
deactivate

echo Iniciando servidor Vue.js...
cd C:\Users\Diego Segovia\Desktop\codes\Proyectos\CImanage2.0\Vue-django\vue-django
npm run serve
