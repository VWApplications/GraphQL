"""
Cada esquema tem um tipo especial chamado Query para obter dados do servidor.

query {
  links {
    id
    description
    url
  }
}
"""

from .types import LinkType
from .models import Link
import graphene


class LinkQuery(graphene.ObjectType):
    """
    Tipo especial de consulta que obtem dados do servidor.
    """

    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        """
        Cada campo é manipulado por meio de resolvers, que retornam um valor.
        """

        return Link.objects.all()