#!/usr/bin/python
# This Python file uses the following encoding: utf-8

def hello():
   print('Hi NTI300!')
   print('This is Jonathans Python Install Script.')

hello()

import os
def install_apache():
   print('Installing Apache Web Server')
   os.system('sudo yum -y install httpd')

   print('Starting HTTP service')
   os.system('sudo systemctl enable httpd.service')

   print('Starting the Apache Server')
   os.system('sudo systemctl start httpd.service')

   print('Please create an inbound security rule for HTTP to open port 80 on the server.')

install_apache()

import os
def clone_github():
   print('Installing git.')
   os.systen('sudo yum -y install git')

   print('Cloning jwade005s GitHub.')
   os.system('git clone https://github.com/jwade005/install_scripts.git')

clone_github()

import os
def publish_website():
   print('Publishing Website.')
   os.system('sudo sh -c "cat install_scripts/index.html > /var/www/html/index.html"')
   os.system('sudo sh -c "cat install_scripts/page2.html > /var/www/html/page2.html"')

   print('Adjusting Permissions.')
   os.system('sudo chmod 644 /var/www/html/index.html')
   os.system('sudo setenforce 0')

   print('Adjusting http.conf file.')
   os.system('sudo sed -i "151s/None/AuthConfig/1" /etc/httpd/conf/httpd.conf')

   print('Adding .htaccess and .htpasswd files.')
   os.system('sudo sh -c "cat install_scripts/.htaccess > /var/www/html/.htaccess"')
   os.system('sudo sh -c "cat install_scripts/.htpasswd > /var/www/html/.htpasswd"')

   print('Adjusting Permissions.')
   os.system('sudo chmod 644 /var/www/html/.htaccess')
   os.system('sudo chmod 644 /var/www/html/.htpasswd')

   print('Restarting HTTP service.')
   os.system('sudo service httpd restart')

publish_website()

import os
def django_install():
   print('Installing Django Framework.')
   print('Current version of Python:')
   os.system('python --version')

   print('Installing virtualenv to give Django its own version of Python.')
   os.system('sudo rpm -iUvh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm')
   os.system('sudo yum -y install python-pip')
   os.system('sudo pip install virtualenv')
   os.system('cd /opt')
   os.system('sudo mkdir django')
   os.system('sudo chown -R ec2-user django')
   os.system('sleep 5')
   os.system('cd django')
   os.system('sudo virtualenv django-env')

   print('Activating virtualenv.')
   os.system('source /opt/django/django-env/bin/activate')

   print('To switch out of virtualenv type: deactivate.')
   print('Now using this version of Python:')
   os.system('which python')

   print('Adjusting permissions for Django directory.')
   os.system('sudo chown -R ec2-user /opt/django')

   print('Installing Django.')
   os.system('pip install Django')

   print('Django Admin is version:')
   os.system('django-admin --version')

   print('Creating new Django Project.')
   os.system('django-admin startproject Project1')

django_install()

import os
def install(package):
   os.system('sudo yum -y install '+package)

   print('Installing Tree Package')

install('tree')

import os
def project1_dir():
   print('This is the new Project1 directory')
   os.system('tree project1')

   print('Go to https://docs.djangoproject.com/en/1.10/intro/tutorial01/ to begin first Django Project!')

project1_dir()

import os
def start_django():
   print('Starting Django Server.')
   os.system('source /opt/django/django-env/bin/activate')

   print('Adjusting Permissions.')
   os.system('sudo chmod 644 /opt/django/project1/manage.py')

   print('Migrating Database Files.')
   os.system('python manage.py migrate')

start_django()

import os
def mysite():
    print('Installing MySite Django Polling Project from GitHub.')
    os.system('git clone https://github.com/jwade005/mysite.git')

    print('Moving MySite files to Django project directory.')
    os.system('sudo mv mysite /opt/django')

    print('Adjusting permissions for MySite.')
    os.system('sudo chown -R ec2—user /opt/django') 

    print('Polling Site Accessible from the Web.')
    print('Django is now accessible from the web server at serverIP:8000.')
    print('Run command: python manage.py runserver 0.0.0.0:8000')

mysite()

import os
def dirty_cow():
    print('Cloning Dirty Cow Patches from jwade005s GitHub.')
    os.system('cd ~')
    os.system('git clone https://github.com/jwade005/automation_scripts.git')

    print('Running Dirty Cow Patch script.')
    os.system('sudo ./automation_scripts/dirty_cow_patch.sh')

    print('Verifying Dirty Cow Patch success.')
    os.system('sudo ./automation_scripts/verify_dirty_cow_patch.sh')

dirty_cow():

