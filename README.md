# REST-API-con-FastAPI
Desarrollo de una API en Python con el Framework FastAPI

Instalar python: https://www.python.org/
Instalar los siguientes comandos para el gestor de paquetes de python pip:
MAC: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
Linux: sudo apt-get update
 sudo apt-get install python3-pip
 
Instalación del entorno virtual con virtualenv:
·	Dentro de la carpeta FastAPI-CRUD-REST-API, instalar el siguiente comando: pip3 install virtualenv.
·	Ejecutar el siguiente comando dentro de la carpeta FastAPI-CRUD-REST-API, para crear el entorno virtual: python3 –m virtualenv env.
Para activar el entorno virtual ejecutamos los siguientes pasos:
·	En la carpeta FastAPI-CRUD-REST-API ejecutar cd env para acceder a la carpeta del entorno virtual.
·	Ejecutar el comando cd bin.
·	Ejecutar el comando source activate para activar el entorno virtual.
Para instalar el framework FastAPI:
·	En la terminal, dentro de la carpeta FastAPI-CRUD-REST-API, con el entorno virtual activado, se ejecuta el siguiente comando: pip install fastapi.
·	Con el siguiente comando, podremos levantar el servidor: pip install uvicorn.
Levantar el servidor con uvicorn.
·	Con el entorno virtual activado, y ubicandose en la raíz principal de la carpeta del proyecto FastAPI-CRUD-REST-API en el archivo main, ejecutar el siguiente comando para levantar el servidor: uvicorn main:app
·	El servidor se levantará en el puerto y con el siguiente PATH: http://127.0.0.1:8000/docs

<img width="1438" alt="CRUD-REST-API" src="https://user-images.githubusercontent.com/110941389/184259821-3fe0bc34-4cc7-4375-89e5-6f3cd92cb72f.png">
