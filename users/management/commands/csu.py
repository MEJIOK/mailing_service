from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания администратора"""

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email="admin@localhost",
            first_name="Admin",
            is_superuser=True,
            is_active=True,
            is_staff=True,
            password="12345",
        )
        user.set_password("12345")
        user.save()
