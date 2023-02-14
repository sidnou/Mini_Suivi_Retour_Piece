"""
ASGI config for Mini_Suivi_Retour_Piece project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mini_Suivi_Retour_Piece.settings')

application = get_asgi_application()
