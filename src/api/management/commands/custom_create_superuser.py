from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
import os

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser using django superuser environ variables'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        if not all([password, username, email]):
            raise CommandError('Set DJANGO_SUPERUSER environ')
        else:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email,
                                              password=password)
                self.stdout.write(self.style.SUCCESS('USER CREATED'))
            else:
                self.stdout.write(self.style.SUCCESS('USER ALREADY EXISTING'))
