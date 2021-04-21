import graphene
from graphene_django import DjangoObjectType

from apps.book_store.models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "synopsis", "author", "published_date")


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()
