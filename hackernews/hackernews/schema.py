import graphene

import links.schema
import users.schema


class Queries(links.schema.Query,
              users.schema.Query,
              graphene.ObjectType):
    """
    Esta classe herdará de várias consultas quando começarmos a adicionar
    mais aplicativos ao nosso projeto.
    """

    pass

class Mutations(links.schema.Mutation,
                users.schema.Mutation,
                graphene.ObjectType):
    """
    Esta classe herdará de várias mutações quando começarmos a adicionar
    mais aplicativos ao nosso projeto.
    """

    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)