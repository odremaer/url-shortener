import graphene

import shortenerapp.schema


class Query(shortenerapp.schema.Query, graphene.ObjectType):
    pass


class Mutation(shortenerapp.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)