import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser from environment variables if it does not already exist.'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', '').strip()
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '').strip()
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')

        if not username or not email or not password:
            self.stdout.write(
                self.style.WARNING(
                    'Superuser environment variables are not fully configured; skipping creation.'
                )
            )
            return

        user_model = get_user_model()

        if user_model.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS(f'Superuser "{username}" already exists; skipping creation.')
            )
            return

        if user_model.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.SUCCESS(f'Superuser with email "{email}" already exists; skipping creation.')
            )
            return

        user = user_model.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.stdout.write(
            self.style.SUCCESS(f'Superuser "{user.username}" created successfully.')
        )
