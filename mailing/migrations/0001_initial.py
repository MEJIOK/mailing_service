# Generated by Django 4.2 on 2024-08-14 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=35, unique=True, verbose_name="Почта"),
                ),
                (
                    "family_name",
                    models.CharField(max_length=50, verbose_name="Фамилия"),
                ),
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                (
                    "middle_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Отчество"
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Коммент"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активность"),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "start_mailing",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Начало рассылки",
                    ),
                ),
                (
                    "next_mailing",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Следующая рассылка",
                    ),
                ),
                (
                    "end_mailing",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Конец рассылки",
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("once_day", "раз в день"),
                            ("once_week", "раз в неделю"),
                            ("once_month", "раз в месяц"),
                        ],
                        max_length=100,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("created", "создана"),
                            ("executing", "запущена"),
                            ("finished", "закончена успешно"),
                            ("error", "закончена с ошибками"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="активна"),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.CreateModel(
            name="MailingLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_attempt",
                    models.DateTimeField(
                        auto_now=True, verbose_name="дата и время последней попытки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("successfully", "успешно"),
                            ("not_successful", "не успешно"),
                        ],
                        default=None,
                        verbose_name="статус попытки",
                    ),
                ),
                (
                    "server_response",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="ответ почтового сервера",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лог рассылки",
                "verbose_name_plural": "Логи рассылок",
                "ordering": ("-last_attempt",),
                "permissions": [("change_is_active", "Может отключать рассылки.")],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Тема")),
                ("message", models.TextField(verbose_name="Сообщение")),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
    ]
