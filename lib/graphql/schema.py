from graphene import ObjectType, Schema

from apps.book_store.graphql.schema import Query as BookStoreQuery


class Query(BookStoreQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query)
