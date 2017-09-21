import graphene

import celebrityshop.ingredients.schema

from celebrityshop.honey.schema import Query as HoneyQuery
from celebrityshop.purchases.schema import PurchaseMutation, Query as PurchaseQuery


class Query(celebrityshop.ingredients.schema.Query,
            HoneyQuery,
            PurchaseQuery,
            graphene.ObjectType):
    pass


class Mutation(PurchaseMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)