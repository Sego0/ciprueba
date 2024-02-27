@echo off
rem Activar el entorno virtual
call cd venv\Scripts\activate.bat

rem Ejecutar el servidor Django
echo Iniciando servidor Django...
py manage.py runserver

rem Esperar unos segundos para que el servidor Django inicie completamente...
timeout /t 5

rem Desactivar el entorno virtual
deactivate

