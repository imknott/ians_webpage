# ians_webpage
 Django webpage that will hold info about me and help teach others python. 


June 08 2021:

On this day I initialized the begining of the project by making a folder called ians_webpage which I then opened terminal and changed the directory to that folder. Once I arrived in that directory I entered the following code to create a virtual environment for the project:

            python3 -m venv iw_env


once that was done I checked to see if I could activate the enviornment by running: 

            source iw_env/bin/activate

Which then took me in terminal to the acitvated enviornment. 

Inside the virtual environment in terminal I entered the following code to install django. 

            pip install django

In order to create the actual project I ran the code 

            django-admin startproject ians_webpage .

which created the project ians_py_page which should contain the following files: 

__init__.py, settings.py, urls.py, wsgi.py

after this step I created the database for the django application by using the following code in the virtual enviornment in terminal: 

            python3 manage.py migrate

What this did was prepare the database to store information it needs to handle authentication and admin tasks. 

Now I tested to see if the server would run now and what outcome would come from that and this is what I did: 

            python3 manage.py runserver

First it checked to see if my project was set up properly and then it reported the url for my localhost site. When actually putting in the webpage given it just displayed the default django page for a newly made project. 

The next phase I went into was setting up the app ians_py_page which I did by running the code in terminal inside the directory ians_webpage

            source iw_env/bin/activate
            python3 manage.py start_app ians_py_page

inside of the ians_py_page should be the following files:

__init__.py, admin.py, apps.py, migrations, models.py, tests.py, views.py

After this step I went into the models file to start defining what information I wanted a specific model to hold. I decided that I would start by building the blog functionality. Where I will store the values of a given topic and then that topic will store the body of the post.

if you refrence the models file it will hold the code neccessary to make it possible for me the admin to add the topic and body. 

In order to activate the models to be used, I specified the app in the settings.py file within the ians_webpage folder 

        INSTALLED_APPS = [
            #My Apps
            'ians_py_page',

            #Default django apps
            ....
        ]

Next I needed to modify the database to store the given models so I ran the code in terminal inside the virtual enviornment: 

            python3 manage.py makemigrations ians_py_page

which then outputed the text 
-Create model Topic 
-Create model Body

After that I applied the migration using the following inside the same terminal session:

            python3 manage.py migrate

After completing the above steps I ran the process inside the same terminal process as above

            python3 manage.py createsuperuser

Which I specified the Superusers username, email and password. 

Finally in the admin.py file found in the ians_py_page app folder I added the following lines of code: 

            from .models import Topic,Body

            admin.site.register(Topic)
            admin.site.register(Body)

And that was my first day of development and will post my next days steps. 

