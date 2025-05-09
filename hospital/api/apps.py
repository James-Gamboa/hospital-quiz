from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_cliente_group(sender, **kwargs):
    from django.contrib.auth.models import Group

    Group.objects.get_or_create(name='cliente')


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        post_migrate.connect(create_cliente_group, sender=self)
