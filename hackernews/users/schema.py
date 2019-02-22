"""
Schema é uma coleção de Types do tipo Query, Collection e Subscriptions.
Cada esquema tem um tipo especial chamado Query para obter dados do servidor
e Mutation para enviar dados para o servidor e Subscriptions para ter uma conexão
em tempo real com o servidor para ser informado imediatamente sobre eventos importantes.
"""

from .queries import UserQuery
from .mutations import CreateUser
import graphql_jwt
import graphene


class Query(UserQuery):
    """
    Esta classe herdará de várias Queries deste aplicativo.
    """

    pass


class Mutation(graphene.ObjectType):
    """
    Cria uma classe de mutação com os campos a serem resolvidos,
    o que aponta para as nossas mutações definidas.

    mutation {
      tokenAuth(username: "...", password: "...") {
        token
      }
    }

    mutation {
      verifyToken(token: ...) {
        payload
      }
    }

    User o JWT como prefixo no header, ou seja, Authorization: JWT <token>
    """

    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()