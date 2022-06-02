from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

# class MagazineConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'magazine'

class MagazineAppConfig(AppConfig):
    name = 'myproject.apps.magazine' # it defines the module of the current app
    verbose_name = _('Magazine') # it is human readable name which can be translated as well

    def ready(self): # this method imports the signals and activates it
        from . import signals
