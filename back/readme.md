Pasos para ejecutar localmente el back
--------------------------------------

Se parte del repo ya clonado, ubicarse en la carpeta "back".
A modo inicial, se provee la base de datos localmente, para poder comenzar las pruebas, luego del deploy inicial, se cambia la configuración para utilizar el servicio con la base de datos que se vaya a utilizar.

Desde powershell o cmd
pip install poetry

poetry install

poetry shell

python manage.py runserver

