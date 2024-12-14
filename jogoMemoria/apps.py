from django.apps import AppConfig


class GaleriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jogoMemoria'

    
    def ready(self):
        import jogoMemoria.signals
