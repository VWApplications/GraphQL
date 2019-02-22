from django.db import models
from django.conf import settings

class Link(models.Model):
    """
    Links do hacknews
    """
    
    url = models.URLField(
        help_text="Identificador do link"
    )

    description = models.TextField(
        help_text="Descrição do link",
        blank=True
    )

    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE
    )


class Vote(models.Model):
    """
    Votar em um link
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    link = models.ForeignKey(
        Link,
        related_name='votes',
        on_delete=models.CASCADE
    )