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
   os.system('sudo yum -y install git')

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
def tree_install():
	print('Installing tree command.')
	os.system('sudo yum -y install tree')

tree_install()

import os
import subprocess
def django_install():
	print('Installing Django Web Framework.')
	os.chdir('install_scripts')
	os.system('chmod +x django_install')
	subprocess.call(['./django_install'])
	
django_install()

import os
def mysite():
    print('Installing MySite Django Polling Project from GitHub.')
    os.chdir('/home/ec2-user')
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
def crontab():
	print('Creating crontab entry for Server Alert emails every 30 minutes.')
	os.system('(crontab -l 2>/dev/null; echo "0,30 * * * * /home/ec2-user/server_alert3.sh | mail -s "Server Alert" wadejs@icloud.com") | crontab - ')
	os.system('crontab -l')
	
crontab()

import os
import subprocess
def dirty_cow():
    print('Cloning Dirty Cow Patches from jwade005s GitHub.')
    os.chdir('/home/ec2-user')
    os.system('git clone https://github.com/jwade005/automation_scripts.git')

    print('Running Dirty Cow Patch script. Server will reboot - Must verify after reboot.')
    os.system('bash automation_scripts/dirty_cow_patch.sh')

    print('Verifying Dirty Cow Patch success.')
    os.system('bash automation_scripts/verify_dirty_cow_patch.sh')

dirty_cow()
