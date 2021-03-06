# ians_webpage
 Django webpage that will hold info about me and help teach others python. 


June 08 2021:
----------------------------------------------------------------------------

On this day I initialized the begining of the project by making a folder called ians_webpage. First, I opened terminal and used the command -cd to change the directory to that folder. Once I arrived in that directory, I entered the following code to create a virtual environment for the project:

            python3 -m venv iw_env


Once that was done, I checked to see if I could activate the enviornment by running: 

            source iw_env/bin/activate

Which then took me in terminal to the acitvated enviornment. 

Inside the virtual environment in the same terminal session I entered the following code to install django. 

            pip install django

In order to create the actual project I ran the code: 

            django-admin startproject ians_webpage .

which created the project ians_webpage which should contain the following files: 

__init__.py, settings.py, urls.py, wsgi.py

after this step I created the database for the django application by using the following code in the virtual enviornment in terminal: 

            python3 manage.py migrate

What this did was prepare the database to store information it needs to handle authentication and admin tasks. 

Now I tested to see if the server would run now and what outcome would come from that: 

            python3 manage.py runserver

First it checked to see if my project was set up properly, and then it listed the url for the localhost site. When actually putting in the webpage given it just displayed the default django page for a newly made project. 

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


June 10, 2021
----------------------------------------------------------------------------

To start today I refactored the models.py file to no longer hold the model Body or Topic I defined the new models as Author, Blog, and Entry. And to make the changes to our data I ran the terminal and changed directory to our main folder and ran the following: 

            source iw_env/bin/activate
            python3 manage.py makemigrations

After entering the makemigrations the following output was displayed:

            - Create model Author
            - Create model Blog
            - Create model Entry
            - Delete model Body
            - Delete model Topic

Now in order to make the change official I ran the code: 

            python3 manage.py migrate

The following output was displayed: 

            Operations to perform:
  Apply all migrations: admin, auth, contenttypes, ians_py_page, sessions
            Running migrations:

It applied all the changes made and now I could enter the posts from my admin webpage directly. 

Now the way I go about creating web pages for this site is by first defining the URL pattern and then I will write the views and then write the templates. 

So the first step I took in this process was defiing the URL pattern which I did by first inside the urls.py file in ians_webpage folder entering the following code: 

        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('ians_py_page.urls')),
            ]


Once I did that I created a file within the ians_py_page folder called urls.py and inside that file the following code was entered which resembles the file withing ians_webpage under the same name:

        from django.urls import path

        from . import views 

        app_name = 'ians_py_page'
        urlpatterns = [
            #Home page
            path('', views.index, name='index'),
        ]


After this step I went into the views.py file that was autumatically created upon starting the ians_py_page app and entered the following to write a view:

        def index(request):
            """The homepage for ians_py_page"""
            return render(request, 'ians_py_page/index.html')


And after that I created the file index.html to write out the template for the homepage.

