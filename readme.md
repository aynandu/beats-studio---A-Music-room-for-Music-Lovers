This is  a Django - React Webapp of Music System
================================================

Frontend : React&Js
Backend:Python
Framework: Django 
IDE : VS Code
Extesnions used in VScode : 
1. ES7+ React/Redux/React-Native snippets (v4.4.3) by dsznajder
2. Django(v1.15.0) by Baptiste Darthenay
3.Python
4. JavaScript (ES6) code snippets (v1.8.0) by charalampos karypidis
-----------------------------
Reference  
Django DOC: https://github.com/aynandu/InMakes_Learninghub/tree/master/Django/Django/Doc

------------------------------
Firstly, Creating Virtual Environment is a Most Essential part of before starting a Project. open terminal 
-> pip install virtualenv (if not installed)
-> Choose the folder
-> virtualenv env_name
-> env_name/Scripts/activate (for activate venv)
-> deactivate

--------------------------
Once Venv is activated, install django , djangorestframework via terminal in vscode.
-> pip install django djangorestframework (going to install django and djangorestframework seperated)

----------------------
Creating Django Project
--> django-admin startproject project_name

Go to Project Folder
--> cd .\project_name\

Creating Django App, we have two options for that:
--> python manage.py startapp myapp
        This command is run from within the context of a Django project.
        Configuration: It uses the settings and configurations of the Django project that manage.py belongs to.
        Usage: This is the most commonly used command because it ensures that the new app is created with the project's specific settings and configurations.

--> django-admin startapp myapp (choosen here)
        This command can be run outside the context of a Django project.
        Configuration: It does not require a specific Django project to be run and does not use project-specific settings or configurations.
        Usage: This is typically used when you want to create a new app independently of any existing Django project.

