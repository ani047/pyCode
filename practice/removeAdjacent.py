'''def removeAdjacent(lst,l):
    if l==0:
        return lst
    if lst[0]==lst[1]:
        lst.remove(lst[0])
        lst.remove(lst[0])
    removeAdjacent(lst,len(l))

str = input("Str:")
list =[]
for ch in str:
    list.append(ch)
removeAdjacent(list,len(list))
'''
# str = input("Str:")
# list=list()
# for ch in str:
#     list.append(ch)
# length=len(list)
# new=[]
# for i in range(length-1):
#     if list[i]==list[i+1]:
        
    
# print(new)



def removeAdjacent(lst):
    l=len(lst)
    if l==0:
        return 
    if lst[0]==lst[1]:
        lst.remove(lst[0])
        lst.remove(lst[0])
    return removeAdjacent(lst)

str = input("Str:")
list =[]
for ch in str:
    list.append(ch)
removeAdjacent(list)







'''In Django, the wsgi.py file is an entry 
point for the WSGI (Web Server Gateway 
Interface)
 server to communicate with your Django 
 application. WSGI is a standard interface 
 between web servers and web 
 applications/frameworks in Python.

The wsgi.py file is automatically generated
 when you create a new Django project
   using the django-admin startproject 
   command. It is located in the root 
   directory of your Django project.

Here's what typically happens in the 
wsgi.py file:

Importing necessary modules: 
The wsgi.py file starts by importing modules
 required for setting up the WSGI server and
   Django application. These modules may 
   include os, sys, and the 
   get_wsgi_application() function from 
   django.core.wsgi.

Configuring the environment: 
It sets up the environment variables and 
system path to ensure the WSGI server can 
find your Django project and its dependencies. This is done using the os.environ.setdefault() and os.path functions.

Obtaining the Django application object:
 The wsgi.py file then retrieves the Django
   application object by calling the
     get_wsgi_application() function from 
     django.core.wsgi. This function returns
       the WSGI application that will handle 
       incoming requests.

Creating the WSGI server: Finally, the 
wsgi.py file creates the WSGI server object.
 This can be a basic server provided by the 
 web server software
   (e.g., runserver command), or 
   it can be a server provided by a 
   production-ready WSGI server such as 
   Gunicorn or uWSGI.

The wsgi.py file acts as the bridge 
between the web server and your Django
 application. It sets up the necessary
   configurations and provides the entry 
   point for the web server to communicate 
   with your Django project.

Remember, the wsgi.py file is typically 
handled by the web server and doesn't 
require direct modifications unless you have
 specific requirements or need to customize
   the WSGI configuration.'''