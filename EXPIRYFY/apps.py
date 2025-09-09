from django.apps import AppConfig




from django.apps import AppConfig

class EXPIRYFYConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EXPIRYFY'

    def ready(self):
        from . import tasks
        tasks.start()
