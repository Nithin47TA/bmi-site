# BMI-APP

This Web Application was created as part of our collage Python final assignment

## Setting up Development Environment

---

\
**!!Perform The Following Steps Before Cloning The App!!**

To avoid conflit with django app dependecies and local python environment dependencies it is advisable to create a virtual env in your project directory first.
\
\
First create directory(myproject) in you desktop to clone the app

```windows
 myproject/
```

use the git bash command line

cd inside the working directory(myproject) and run the following commands

```bash
python -m venv env(--or any name you want)
```

This command will create a folder with name env(or the name you gave)

```windows
 myproject/
    env
```

After creating virtual env run the following command to use the virtual env

```bash
source env/scripts/activate
```

> this will show (env) in the bash command line after every command indicating the virtual env activation

git clone the application in the current directory myproject

```windows
myproject/
    env/
    bmi/
```

cd into the bmi-site directory and run

```python
pip install -r requirements.txt
```

This will install all the required packages for the application

After that to spin up the server run

```python
python manage.py migrate
```

```python
python manage.py runserver
```

---
