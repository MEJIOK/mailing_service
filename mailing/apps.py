from time import sleep

from django.apps import AppConfig


class MailingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing"

    def ready(self):
        from mailing.management.commands.runapscheduler import start

        sleep(2)
        start()
