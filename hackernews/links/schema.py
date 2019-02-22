"""
Schema é uma coleção de Types do tipo Query, Collection e Subscriptions.
Cada esquema tem um tipo especial chamado Query para obter dados do servidor
e Mutation para enviar dados para o servidor e Subscriptions para ter uma conexão
em tempo real com o servidor para ser informado imediatamente sobre eventos importantes.
"""

from .queries import LinkQuery
from .mutations import CreateLink
import graphene


class Query(LinkQuery):
    """
    Esta classe herdará de várias Queries deste aplicativo.
    """

    pass


class Mutation(graphene.ObjectType):
    """
    Cria uma classe de mutação com os campos a serem resolvidos,
    o que aponta para as nossas mutações definidas.
    """

    create_link = CreateLink.Field()