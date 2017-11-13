# Density-X Heroku deployment

This app was created on top of python-getting-started. The readme for the original infrastructure is below.

## Test on your local.

Create a virtual environment to test the app on your local machine.

```sh
$ conda env export -n venv
$ source activate venv
$ pip install -r requirements.txt
```

Then run the thing...
```sh
$ python manage.py collectstatic
```
(answer yes)

```sh
$ heroku local web
```

Now access the local deployment at http://localhost:5000

If you are having issues getting this to run, your 5000 port may be busy. Kill all processes on that port with:
```sh
$ kill `lsof -i :5000`
```

##Push changes and deploy on Heroku.
```sh
$ git add .
$ git commit -m "commit message"
$ git push heroku master
$ heroku open
```

Done forget to also push to github (here; origin master) where you should definitely also be saving these files:
```sh
$ git add .
$ git commit -m "commit message"
$ git push origin master
```

##The file structure
The file /uploads/core/view.py is where your python code (the actual code being deployed, in this case DensityX.py) lives.

The file /uploads/templates/base.html is the base html file that is essentially your index.html file. All other html files extend base.

The file /uploads/core/templates/core/home.html is where the stuff on your index page is defined. For example, the upload button in DensityX is defined here.

##Some files you'll need
Use python-getting-started from heroku for an example of a working setup with all required files (readme for original is below)

requirements.txt file - all dependencies and versions go here. To get version: run python, import module, type:
```sh
$ print module.__version__
```

urls.py - list of all the "pages" on the web interface

view.py - where the actual python code gets called and executed. The script to run must be wrapped as a function like:
```sh
def my_python_script(some_thing)
```

# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
