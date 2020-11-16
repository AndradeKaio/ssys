from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'ssys'
            password = 'password'
            email = 'user@ssys.com.br'
            user = User.objects.create_superuser(email=email, username=username, password=password)
            user.save()
            print("User created!")