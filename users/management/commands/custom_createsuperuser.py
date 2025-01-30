from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Command(BaseCommand):
    help = 'Create a superuser with additional fields'

    def handle(self, *args, **options):
        email = input('email: ')
        name = input('Name: ')
        password = input('password: ')
        password2 = input('password again: ')
        if password != password2:
            raise CommandError("password do not match")
        user_model = get_user_model()
        if user_model.objects.filter(email=email).exists():
            raise CommandError("User with this email already exists")
        user_model.objects.create_superuser(name=name, email=email, password=password)
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))