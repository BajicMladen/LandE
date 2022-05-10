from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'
    verbose_name = 'users'

    def ready(self) -> None:
        from django.core.cache import cache
        cache.clear()
