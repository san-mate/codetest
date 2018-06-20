Code Test
=========

Questions
---------

Questions can be runned by::

    $ python 1_question.py
    $ python 2_question.py


Django Project
--------------

Inside the 'activityfeed' you will finde a Django 1.11 project, with django rest
framework to serve json, and also sqlite db that have two users and two Posts uploaded. Users 'admin' and  'user1',
password for both '1234qwer'.

To run the project follow this steps.

1. Install requirements by::

    $ pip install -r requirements.txt

2. Run server::

    $ python manage.py runserver

3. Go to the admin:

    * http://localhost:8000/admin/

4. Login with one of the users already there, or create a new from console to login::

    $ python manage.py createsuperuser

5. Test the endpoints:

    * http://localhost:8000/posts/
    * http://localhost:8000/posts/me/
    * http://localhost:8000/posts/followed/
