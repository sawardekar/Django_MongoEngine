MongoEngine

This Project we will cover how to connected MongoDB Database in Django and
Create, Update, Delete record in MongoDB database using APIView and Viewset function.

Installed Required Packeages
pip install djongo
pip install djangorestframework 
pip install django-mongoengine
pip install django-rest-framework-mongoengine
pip install mongoengine
pip install pymongo

Note:
python manage.py makemigrations command run no changes applied
python manage.py migrate command not appliable on django custom model only applied on default model such as Auth user, group, permission.

Django Mongoengine admin page are different to default django admin page
127.0.0.1:8000/admin  ---> default admin page
127.0.0.1:8000/mongoadmin/ --> Mongoengine admin Page
Both admin page in username and password are same.


More detail you can refer below video
https://www.youtube.com/watch?v=nZx4NE8ltDE


Employee import data format
{
     "name": "sanket",
     "username": "sanket.sawardekar",
     "email": "sanket@gmail.com",
     "emp_id": 1003,
     "designation":{
         "name": "Programmer"
     }
}

list of mongoengine fields ref below link
https://github.com/umutbozkurt/django-rest-framework-mongoengine/blob/master/rest_framework_mongoengine/serializers.py


Install MongoDB server
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

Install MongoDB Compass 
https://www.mongodb.com/download-center/community?jmp=docs
