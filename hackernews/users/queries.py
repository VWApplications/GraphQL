"""
Cada esquema tem um tipo especial chamado Query para obter dados do servidor.

query {
  users {
    id
    username
    email
  }
}
"""

from django.contrib.auth import get_user_model
from .types import UserType
import graphene


class UserQuery(graphene.ObjectType):
    """
    Tipo especial de consulta que obtem dados do servidor.
    """

    users = graphene.List(UserType)

    def resolve_users(self, info):
        """
        Cada campo é manipulado por meio de resolvers, que retornam um valor.
        """

        User = get_user_model()

        return User.objects.all()