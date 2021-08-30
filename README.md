# Cookiecutter Django

Open-source `cookiecutter` template built on top of a simple Django codebase with a Bootstrap 5 design - Features:

- UI Kit: **Volt Dashboard** (Lite Version) Bootstrap 5 design provided by **Themesberg**
- SQLite Database, Django Native ORM
- Modular design, clean codebase
- Session-Based Authentication, Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

> Links

- [Django Bootstrap 5 Volt](https://appseed.us/admin-dashboards/django-dashboard-volt) - product page
- [Django Bootstrap 5 Volt](https://django-volt-dashboard.appseed-srv1.com/) - LIVE deployment

<br />

![Django Bootstrap 5 Volt - Template project provided by AppSeed.](https://raw.githubusercontent.com/app-generator/django-dashboard-volt/master/media/django-dashboard-volt-intro.gif)

<br />

## How to use it

<br />

### **Using cookiecutter**  

> **Step #1** - Create a virtual environment  

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate

```

<br />

> **Step #2** - Install Depenedencies 

```bash
$ # Install modules - SQLite Storage
$ pip3 install cookiecutter
```

<br />

> **Step #3** - Generate the project 

```bash
$ cookiecutter https://github.com/app-generator/cookiecutter-django.git
```

The project is generated in the current working directory. 

<br />

### Using **appseed-shell** package 

> **Step #1** - Install `appseed-shell` 

```bash
$ # Start the application (development mode)
$ pip3 install appseed-shell
```

<br />

> **Step #2** - Launch the Python shell and generate the product

```python
$ python
>>> from appseed_shell import generate_django
>>> generate_django()
```

The project is generated in the current working directory. 

<br />

## Credits & Links

For more resources and support please access: 

- [AppSeed](https://appseed.us) - For more starters and support
- [AppSeed Shell](https://github.com/app-generator/appseed-shell-py) - source code (MIT License)

<br />

---
Cookiecutter Django - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
