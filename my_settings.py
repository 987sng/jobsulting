from web1.settings import DATABASES
DATABASES = { 
	'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'Saramin', 
        'USER': 'root', 
        'PASSWORD': '', 
        'HOST': 'localhost', 
        'PORT': '3306', 
     } 
}