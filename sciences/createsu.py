
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='alromy').exists():
            User.objects.create_superuser(
                username='alromy',
                password='3s77t00p@ertert77'
            )
        print('Superuser has been created.')