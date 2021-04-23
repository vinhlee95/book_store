import graphene

from apps.book_store.models import Book, Author
from apps.book_store.graphql.types import BookType


class BookInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    synopsis = graphene.String(required=True)
    author_name = graphene.String(required=True)


class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    # Fields of the Mutation when it is resolved
    ok = graphene.Boolean()
    book = graphene.Field(lambda: BookType)

    def mutate(self, info, book_data: BookInput = None):
        if not book_data:
            raise Exception("No book data provided.")

        author = Author.objects.get(name=book_data.author_name)
        new_book = Book(title=book_data.title, synopsis=book_data.synopsis, author=author)
        new_book.save()
        return CreateBook(ok=True, book=new_book)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
