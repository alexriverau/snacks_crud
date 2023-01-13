# Lab: 29 - Custom User Model / Tailwind CSS / Flowbite
# Lab: 28 - Django CRUD

---

### Project: Snacks
### Author: Alejandro Rivera

---

Django project that builds a "snacks" application.

* v1.1
  * Updates the administration users in the "snacks" app. 
  * Implements a custom user model.
  * Adds styling with Tailwind CSS / Flowbite. 
  * Creates `.env` file 
* v1.0
  * Adds full CRUD functionality. Allows user to Create, Read, Update and Delete "snacks". 

### Setup

* Install dependencies in a `venv`
  * **run:** pip install -r requirements.txt
* Dependencies: 
  * [requirements.txt](requirements.txt)
* Update `.env` file with secret key 

### How to initialize/run your application

* Initialize server:
  * **run:** python3 manage.py runserver

* Go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 

### Links and Resources

* app page: [snacks](http://127.0.0.1:8000/)
* admin page: [snacks_admin](http://127.0.0.1:8000/admin)
  * email: admin@admin.com
  * password: django

### Tests

* **run:** python3 manage.py test