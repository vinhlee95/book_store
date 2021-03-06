from graphene import ObjectType, Schema, Field
from graphene_django.debug import DjangoDebug

from apps.book_store.graphql.schema import Query as BookStoreQuery, Mutation as BookStoreMutation


class Query(BookStoreQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    debug = Field(DjangoDebug, name='_debug')
    pass


schema = Schema(query=Query, mutation=BookStoreMutation)
