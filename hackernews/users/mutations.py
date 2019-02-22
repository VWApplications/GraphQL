"""
Cada esquema tem um tipo especial chamado Mutation para enviar dados para o servidor.

mutation {
  createUser(
    username: "victorhad",
    email: "victorhad@gmail.com",
    password: "django1234"
  ) {
    user {
      id
      username
      email
    }
  }
}
"""

from .types import UserType
from django.contrib.auth import get_user_model
import graphene


class CreateUser(graphene.Mutation):
    """
    Define a saída da mutação, ou seja, ao criar um usuário
    irá ter como resultado o todos os campos do usuário
    definido no UserType.
    """

    user = graphene.Field(UserType)

    class Arguments:
        """
        Define os dados que você pode enviar para o servidor.
        """

        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        """
        Cria um usuário no banco de dados usando os dados
        enviados pelos argumentos, e retorna a classe
        CreateUser com os dados que acabaram de ser criados.
        """

        user = get_user_model()(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save()

        return CreateUser(user=user)