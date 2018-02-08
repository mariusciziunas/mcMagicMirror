import django
import os

print('Creating user admin...')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mcMagicMirror.settings'
django.setup()

from django.contrib.auth.models import User

username = 'admin'
password = 'mcadmin'
admin = User.objects.get(username=username)
if admin is None:
    User.objects.create_superuser(username=username, password=password, email='')
    print('User created')
else:
    print('User ' +  username + ' already exists')

