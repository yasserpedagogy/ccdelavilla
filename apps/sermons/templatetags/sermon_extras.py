# apps/sermons/templatetags/sermon_extras.py
from django import template
import re

register = template.Library()


@register.filter
def youtube_embed_url(value):
    """Convierte URL de YouTube a formato embed"""
    if not value:
        return value

    # Patrones comunes de YouTube
    patterns = [
        r"youtube\.com/watch\?v=([^&]+)",
        r"youtu\.be/([^?]+)",
        r"youtube\.com/embed/([^?]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, value)
        if match:
            video_id = match.group(1)
            return f"https://www.youtube.com/embed/{video_id}"

    return value
