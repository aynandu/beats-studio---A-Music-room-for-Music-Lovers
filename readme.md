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
--------------------------
---> React Portion :
api app for the backend and frontend app for the other. react is  frontend for that create src folder also create component folder init. then
     -> npm init -y 
            (which install package.json in the frontend folder,which contains the version detals)
     -> npm i webpack webpack-cli --save-dev 
            (install webpack.which install package-l0ck.json in the frontend folder)
     -> npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev

            (Babel is often used in React projects to transform JSX syntax into regular JavaScript.Babel is a popular JavaScript compiler that allows developers to write code using the latest JavaScript features and syntax, which may not be natively supported by all browsers or environments. Babel transforms this code into a version that is compatible with older browsers and environments, ensuring wider compatibility and functionality.After this node_modules folder will installed)
     -> npm i react react-dom --save-dev
     -> npm install @material-ui/core 
            (for ui like cards grids etc similar to bootstrap. this is a  Material-UI v4 not compatible with react 18.there should be a error.
            so use "-> npm install @mui/material @emotion/react @emotion/styled " for Material-UI v5 or "-> npm install @material-ui/core --legacy-peer-deps" for bypass it and use Material-UI v4 or downgrade the react )
     -> npm install @babel/plugin-proposal-class-properties 
        (Due to compactible issue this is not currently using.  instead use this " -> npm install @babel/plugin-transform-class-properties" for older version "-> npm install @babel/plugin-transform-class-properties --legacy-peer-deps")
     -> npm  install react-router-dom 
            (This is used to reload pages. if facing compatible issue use '--legacy-peer-deps' at the end. like "-> npm install react-router-dom --legacy-peer-deps" )
     -> npm install @material-ui/icons
            ( if facing compatible issue use '--legacy-peer-deps' at the end. like "-> npm install @material-ui/icons --legacy-peer-deps")
    create a babel.config.json & webpack.config.js (bundle all the js file into one file ) file. After that change in the "scripts" field on package.json for run.
--------------------------
Tips :
 * Makesure every app you created. always add it in the INSTALLED_APPS in project settings
 * when ever there is a change in db, models.py and settings.py from project update do :
    -> python manage.py makemigrations
    -> python manage.py migration
* run your webApp use :
    -> python manage.py runserver
* Serilizer class (serializers.py):  what seiliazer does is it will take our model it has all the python related codes, it will transilate this models classes into a json response. ie keys and values. --> from rest_framework import serializers
* Generics : what will it do a class inherits from a generic API view -> from rest_frameworks import generics.generics.CreateAPIView : can create /add data on front along with shows the datas as json format. otherhand generics.ListAPIView :shows the datas as json format only.
------------------

