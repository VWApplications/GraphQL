"""
Type é um objeto que pode conter vários campos.
E está associado a um modelo.
"""

from graphene_django import DjangoObjectType
from .models import Link


class LinkType(DjangoObjectType):
    """
    Objeto com todos os campos da modelo Link
    """

    class Meta:
        model = Link