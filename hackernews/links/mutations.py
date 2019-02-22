"""
Cada esquema tem um tipo especial chamado Mutation para enviar dados para o servidor.

mutation {
  createLink(
    url: "http://www.github.com",
    description: "Lots of code"
  ) {
    id
    url
    description
  }
}
"""

from .models import Link
import graphene

class CreateLink(graphene.Mutation):
    """
    Define a saída da mutação, ou seja, ao criar um link
    irá ter como resultado o ID, url e description.
    """

    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    class Arguments:
        """
        Define os dados que você pode enviar para o servidor,
        nesse caso, o URL e a descrição dos links.
        """

        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        """
        Cria um link no banco de dados usando os dados
        enviados pelos argumentos, e retorna a classe
        CreateLink com os dados que acabaram de ser criados.
        """

        link = Link(
            url=url,
            description=description
        )

        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )