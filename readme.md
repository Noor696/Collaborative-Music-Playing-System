* `pip install django djangorestframework`

* `django-admin startproject <project_name> .` 

in my project :

`django-admin startproject music_controller .`

* Create App command: 
`django-admin startapp <app_name>`

I have Apps in my project:
1. api app `django-admin startapp api` to handle API. 
2. rest_framework `django-admin startapp rest_framework`

* Add the App I created to Project in sitting file.

* Update the DB

`python manage.py makemigrations`
`python manage.py migrate`

* To run the server
`python manage.py runserver`


-----------------

* Make **Frontend app** -> Add Templates folder -> Add static folder (inside it make css , frontend, images folder) -> src folder.

* `npm init -y` -> is going to create a node modules, package.JSON and all the other thing we need for frontend project.

* **webpack** is going to do is take all of our source javaScript stuff and transpilot or bundle it into one single JavaScript file 
 `npm install webpack webpack-cli --save-dev`

* install Bable -> will take our code and transpilot into code that is friendly with all different types of browsers (older and newer)
`npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev`
then :
`npm install @babel/plugin-proposal-class-properties` -> the reason we need this is we can use async and await in JavaScript code. it's kind of strange that we need to add that.

* install react `npm i react react-dom --save-dev`

* install material UI -> this is just some prebuilt component that we can use to a void having to style the webpage ourself. / built in component and have the nice things like cards and grids and all that. it's kind of similar to something like bootstrab.
`npm install @material-ui/core`
`npm install @material-ui/icons`

* install react router `npm install react-router-dom` -> this going to allow us to reroute the pages 

