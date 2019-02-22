"""
Type é um objeto que pode conter vários campos.
E está associado a um modelo.
"""

from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    """
    Objeto com todos os campos da modelo User
    """

    class Meta:
        model = get_user_model()