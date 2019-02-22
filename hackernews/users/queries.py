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
from graphql import GraphQLError
from .types import UserType
import graphene


class UserQuery(graphene.ObjectType):
    """
    Tipo especial de consulta que obtem dados do servidor.
    """

    users = graphene.List(UserType)
    current_user = graphene.Field(UserType)

    def resolve_users(self, info):
        """
        Cada campo é manipulado por meio de resolvers, que retornam um valor.
        """

        User = get_user_model()

        return User.objects.all()

    def resolve_current_user(self, info):
        """
        Pega o usuário logado.
        """

        user = info.context.user
        
        if user.is_anonymous:
            raise GraphQLError("Not logged in")

        return user