import graphene

from apps.book_store.models import Book, Author
from apps.book_store.graphql.types import BookType


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        synopsis = graphene.String()
        author_name = graphene.String()

    # Fields of the Mutation when it is resolved
    ok = graphene.Boolean()
    book = graphene.Field(lambda: BookType)

    def mutate(self, info, title, synopsis, author_name):
        author = Author.objects.get(name=author_name)
        new_book = Book(title=title, synopsis=synopsis, author=author)
        new_book.save()
        return CreateBook(ok=True, book=new_book)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
