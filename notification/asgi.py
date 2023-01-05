"""
ASGI config for notification project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

import main_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websoket': AuthMiddlewareStack(
    URLRouter(
      main_app.routing.websocket_urlpatterns
    )
  )
})
