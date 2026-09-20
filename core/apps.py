from django.apps import AppConfig, apps
from django.contrib import admin


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Auto-register every model from every app that doesn't already have
        # a custom ModelAdmin, so the admin site stays complete with zero
        # per-model boilerplate. Apps wanting custom behavior can still
        # register their own ModelAdmin in their admin.py — this only fills
        # the gaps. Runs after django.contrib.admin's autodiscover (core is
        # listed after it in INSTALLED_APPS), so explicit registrations win.
        for model in apps.get_models():
            try:
                admin.site.register(model)
            except admin.sites.AlreadyRegistered:
                pass
