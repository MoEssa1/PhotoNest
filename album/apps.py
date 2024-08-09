from django.apps import AppConfig


class AlbumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'album'

    # this will ensure the signals.py file gets imported
    def ready(self):
        import album.signals 
