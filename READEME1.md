 here are the steps on how to create a save the date website using Django Python in a virtual env:

<link rel="stylesheet" href="{% static 'css/datepicker.css' %}">
    <script src="{% static 'js/bootstrap-datepicker.js' %}"></script>
    
Create a virtual environment for your Django project.
python -m venv venv
Windows
Install virtualenv
pip install virtualenv

Move into Scripts directory
cd C:\Python27\Scripts
Create a virtual env.
python virtualenv.exe my_env

Activate the virtual environment.
cd E:\NAREN\automation\django-projects\save-the-date
source venv/bin/activate
WINDOWS - venv\Scripts\activate.bat
cd E:\NAREN\automation\django-projects\save-the-date\save_the_date\mysite

(venv) E:\NAREN\automation\django-projects\save-the-date\save_the_date\mysite>python manage.py runserver

Install Django in your virtual environment.
pip install django
Create a Django project in your virtual environment.
django-admin startproject mysite
Create a Django application for your save the date website in your virtual environment.
python manage.py startapp save_the_date
Add the following code to your save_the_date/models.py file:
Python
from django.db import models

class SaveTheDate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name
Use code with caution. Learn more
Add the following code to your save_the_date/forms.py file:
Python
from django.forms import ModelForm

class SaveTheDateForm(ModelForm):
    class Meta:
        model = SaveTheDate
        fields = '__all__'
Use code with caution. Learn more
Add the following code to your save_the_date/views.py file:
Python
from django.shortcuts import render, redirect
from .forms import SaveTheDateForm

def save_the_date(request):
    if request.method == 'POST':
        form = SaveTheDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('save_the_date_success')
    else:
        form = SaveTheDateForm()
    return render(request, 'save_the_date.html', {'form': form})

def save_the_date_success(request):
    return render(request, 'save_the_date_success.html')
Use code with caution. Learn more
Create a template for your save the date website in your virtual environment.
mkdir save_the_date/templates
touch save_the_date/templates/save_the_date.html
Add the following code to your save_the_date/templates/save_the_date.html file:
HTML
<!DOCTYPE html>
<html>
<head>
    <title>Save the Date</title>
</head>
<body>
    <h1>Save the Date</h1>
    {% if form %}
        <form action="{% url 'save_the_date' %}" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Save the Date">
        </form>
    {% else %}
        <p>There are no save the dates yet.</p>
    {% endif %}
</body>
</html>
Use code with caution. Learn more
Deploy your website to a web server.
You can deploy your website to a web server using a variety of methods. Here are a few options:

Use a hosting service like Heroku or DigitalOcean.
Use a local web server like Apache or Nginx.
Use a cloud-based development environment like Docker or Vagrant.
I hope this helps!

Sources
medium.com/@django.course/why-django-is-the-best-web-framework-for-charting-uncharted-territory-db5222c37d5d
=======================================

here are the steps on how to deploy this Django app locally and start it:

In your virtual environment, run the following command to migrate your database:
python manage.py migrate
Run the following command to start your Django development server:

python manage.py runserver

This will start your Django development server at http://localhost:8000/. You can now access your save the date website at this URL.

To stop the Django development server, press Ctrl+C in your terminal.

Here is a breakdown of what each command does:

python manage.py migrate tells Django to create the tables in your database that are defined by your models.
python manage.py runserver starts the Django development server. This server is used to test your Django application locally before you deploy it to a production server.


packages to install
pip install django-bootstrap-datepicker-plus
pip install django-bootstrap4
pip install django-bootstrap-datepicker-plus
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
