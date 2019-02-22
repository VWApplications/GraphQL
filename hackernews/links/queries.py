"""
Cada esquema tem um tipo especial chamado Query para obter dados do servidor.

query {
  links {
    id
    description
    url
    postedBy {
      id
      username
    }
  }
}
"""

from .types import LinkType, VoteType
from .models import Link, Vote
from django.db.models import Q
import graphene


class LinkQuery(graphene.ObjectType):
    """
    Tipo especial de consulta que obtem dados do servidor.
    """

    links = graphene.List(
      LinkType,
      search=graphene.String(),
      first=graphene.Int(),
      skip=graphene.Int()
    )
    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
        """
        Cada campo é manipulado por meio de resolvers, que retornam um valor.
        """

        query = Link.objects.all()

        if search:
            link_filter = (
                Q(url__icontains=search) |
                Q(description__icontains=search)
            )
            query = query.filter(link_filter)

        if skip:
            query = query[skip:]

        if first:
            query = query[:first]

        return query

    def resolve_votes(self, info, **kwargs):
        """
        Pega todos os votos
        """

        return Vote.objects.all()