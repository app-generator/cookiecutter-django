# Cookiecutter Django

**[Django Cookie-Cutter](https://blog.appseed.us/django-cookie-cutter-generator/)** is an open-source `cookiecutter` template built on top of a simple **Django** codebase with a modern design. For newcomers, **Cookiecutter** is a command-line utility that creates projects from project templates and Django is a leading web framework built by experts using a batteries-included concept.

- UI Themes: `Volt Design` / `Soft UI` / `Datta Able` / `Material Dashboard`
- Persistence: SQLite / MySql / PostgreSQL 
- Modular design, clean codebase
- Session-Based Authentication, Forms validation
- Deployment scripts: `Gunicorn` / `Nginx`
- One-line **Docker** setup
  - `` 

<br />

> Project Customization:

- Project information: `name`, `author`, `email`
- Database Engine: `SQLite`, `MySql` or `PostgreSql`
- UI Themes:
  - [Volt Bootstrap](https://django-volt-dashboard.appseed-srv1.com/) - LIVE Preview
  - [Soft UI](https://django-soft-ui-dashboard.appseed-srv1.com/) - LIVE Preview
  - [Datta Able](https://django-datta-able.appseed-srv1.com/) - LIVE Preview 
  - [Material Dashboard](https://django-material-dashboard.appseed-srv1.com/) - LIVE Preview

<br />

> Links

- [Django Dashboards](https://appseed.us/admin-dashboards/django) - index provided by AppSeed
- [Open-Source Dashboards](https://appseed.us/admin-dashboards/open-source) - crafted in **Flask**, **Django**, [React](https://appseed.us/apps/react)
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

![Django Bootstrap 5 Volt - Template project provided by AppSeed.](https://raw.githubusercontent.com/app-generator/django-dashboard-volt/master/media/django-dashboard-volt-intro.gif)

<br />

## How to use it

<br />

### Using `cookiecutter` tool 

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
$ pip3 install -r requirements.txt
```

<br />

> **Step #3** - Generate the project 

```bash
$ cookiecutter https://github.com/app-generator/cookiecutter-django.git
```

<br />

### Using `appseed-shell` package 

> **Step #1** - Install Dependencies

```bash
$ pip3 install cookiecutter
$ pip3 install GitPython
$ pip3 install appseed-shell
```

<br />

> **Step #2** - Launch the Python shell and generate the product

```python
$ python
>>> from appseed_shell import generate_django
>>> generate_django()
```

<br />

## Credits & Links

For more resources and support please access: 

- [AppSeed](https://appseed.us) - For more starters and support
- [AppSeed Shell](https://github.com/app-generator/appseed-shell-py) - source code (MIT License)

<br />

---
**[Django Cookie-Cutter](https://blog.appseed.us/django-cookie-cutter-generator/)** - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
