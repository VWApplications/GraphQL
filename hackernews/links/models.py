from django.db import models

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