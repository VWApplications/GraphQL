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
    postedBy {
      id
      username
      email
    }
  }
}
"""

from users.types import UserType
from .types import LinkType
from .models import Link, Vote
from graphql import GraphQLError
import graphene

class CreateLink(graphene.Mutation):
    """
    Define a saída da mutação, ou seja, ao criar um link
    irá ter como resultado o ID, url e description.
    """

    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

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

        user = info.context.user or None

        if user.is_anonymous:
          raise GraphQLError("O usuário deve ta logado para criar um link!")

        link = Link(
            url=url,
            description=description,
            posted_by=user
        )

        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by
        )


class UpdateLink(graphene.Mutation):
    """
    Atualiza os dados de um link
    """

    link = graphene.Field(LinkType)

    class Arguments:
        """
        Corpo da requisição
        """

        linkID = graphene.Int()
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, linkID, url, description):
        """
        Atualiza os dados de um link no banco de dados
        e retorna a classe UpdateLink com os dados que
        acabaram de ser atualizados.
        """

        user = info.context.user or None

        if user.is_anonymous:
            raise GraphQLError("O usuário deve ta logado para atualizar o link!")

        link = Link.objects.get(id=linkID)

        if link.posted_by != user:
            raise GraphQLError("Somente o usuário que criou o link pode edita-lo.")

        link.url = url
        link.description = description

        link.save()

        return UpdateLink(link=link)


class DeleteLink(graphene.Mutation):
    """
    Deleta um determinado link
    """

    msg = graphene.String()

    class Arguments:
        """
        Corpo da requisição
        """

        linkID = graphene.Int()

    def mutate(self, info, linkID):
        """
        Atualiza os dados de um link no banco de dados
        e retorna a classe UpdateLink com os dados que
        acabaram de ser atualizados.
        """

        user = info.context.user or None

        if user.is_anonymous:
            raise GraphQLError("O usuário deve ta logado para deletar o link!")

        link = Link.objects.get(id=linkID)

        if link.posted_by != user:
            raise GraphQLError("Somente o usuário que criou o link pode deleta-lo.")

        msg = "Link {0} deletado com sucesso".format(link.id)

        link.delete()

        return DeleteLink(msg=msg)


class CreateVote(graphene.Mutation):
    """
    Cria um voto de um determinado link
    """

    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        """
        Corpo da requisição
        """

        link_id = graphene.Int()

    def mutate(self, info, link_id):
        """
        Método responsável por criar o voto.
        """

        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError('Você deve está logado para votar!')

        link = Link.objects.filter(id=link_id).first()

        if not link:
            raise GraphQLError('Link invalido!')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)