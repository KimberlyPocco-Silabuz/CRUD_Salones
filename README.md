# Añadir el archivo .env
Crear a la altura de la raiz del proyecto el archivo .env con el siguiente contenido
```bash
FLASK_APP = main.py
FLASK_DEBUG = 1
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/crud_colegio'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'esta-es-una-clave-secreta'
```
# Flask docs

Doc for setting up Flask

## Setup

### Install Python

Install Python 3.10

### Install pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Install Flask

```bash
pip install Flask
```

### Install virtualenv

Virtualenv una herramienta para crear entornos virtuales de Python. Esto es útil para aislar las dependencias de un proyecto de las dependencias de otros proyectos.

```bash
pip install virtualenv
```

### Crear una maquina virtual

```bash
virtualenv venv --python=python3.10
```

### Activar la maquina virtual

```bash
source venv/bin/activate
```

- windows

```bash
venv\Scripts\activate

venv/Scripts/activate.ps1
```

### Varaible Flask

Unix

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

window

```bash
set FLASK_APP=app.py
set FLASK_DEBUG=1
```

### Run

```bash
flask run
```

### End virtualenv

```bash
deactivate
```

### Requirements

Si han clonado un proyecto de github y quieren instalar las dependencias, pueden usar el archivo requirements.txt

```bash
pip install -r requirements.txt
```


