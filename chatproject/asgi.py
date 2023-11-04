import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from chatapp.routing import websocket_urlpatterns

import chatapp.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatproject.settings")
django_asgi_app = get_asgi_application()



application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application(),
        "websocket" : AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        )
    }
) 