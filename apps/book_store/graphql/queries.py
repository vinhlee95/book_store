import graphene
from graphene_django.filter import DjangoFilterConnectionField

from apps.book_store.graphql.types import CatType, AuthorConnection, BookConnection
from apps.book_store.models import Author, Book


class Query(graphene.ObjectType):
    authors = graphene.relay.ConnectionField(AuthorConnection)
    books = graphene.relay.ConnectionField(BookConnection)
    node = graphene.relay.Node.Field()
    get_cat = graphene.Field(type=CatType)

    @staticmethod
    def resolve_get_cat(self, info):
        return {"name": "foo", "age": 2, "breed": "bar"}

    @staticmethod
    def resolve_authors(self, info):
        return Author.objects.prefetch_related("books").all()

    @staticmethod
    def resolve_books(self, info):
        return Book.objects.prefetch_related("author").all()
