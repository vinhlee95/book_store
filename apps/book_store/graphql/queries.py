import graphene
from graphene_django.filter import DjangoFilterConnectionField

from apps.book_store.graphql.types import AuthorNode, BookNode, CatType


class Query(graphene.ObjectType):
    authors = DjangoFilterConnectionField(AuthorNode)
    books = DjangoFilterConnectionField(BookNode)
    node = graphene.relay.Node.Field()
    get_book_by_title = graphene.Field(type=BookNode, title=graphene.String(required=True))
    get_cat = graphene.Field(type=CatType)

    def resolve_get_cat(self, info):
        return {"name": "foo", "age": 2, "breed": "bar"}


