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
    books = graphene.List(BookType)
    get_book_by_title = graphene.Field(type=BookType, title=graphene.String(required=True))

    def resolve_authors(self, info):
        return Author.objects.all()

    def resolve_books(self, info):
        return Book.objects.all()

    def resolve_get_book_by_title(self, info, title):
        try:
            return Book.objects.get(title=title)
        except Book.DoesNotExist:
            return None
