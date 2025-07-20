from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import environ

class Command(BaseCommand):
    help = 'Creates initial superuser using django-environ'

    def handle(self, *args, **options):
        User = get_user_model()
        env = environ.Env()

        # Skip if superuser exists
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.WARNING('Superuser exists - skipping'))
            return

        # Get credentials with error handling
        try:
            User.objects.create_superuser(
                username=env('DJANGO_SUPERUSER_USERNAME'),
                email=env('DJANGO_SUPERUSER_EMAIL'),
                password=env('DJANGO_SUPERUSER_PASSWORD')
            )
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        except environ.ImproperlyConfigured:
            self.stdout.write(self.style.ERROR(
                'Missing DJANGO_SUPERUSER_* environment variables'
            ))