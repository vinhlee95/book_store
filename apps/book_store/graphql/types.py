import graphene
import graphene_django_optimizer as gql_optimizer

from apps.book_store.models import Author, Book
from apps.book_store.graphql.loaders import author_loader


class AuthorNode(gql_optimizer.OptimizedDjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name")
        filter_fields = ["id", "name"]
        interfaces = (graphene.relay.Node,)


class BookNode(gql_optimizer.OptimizedDjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "synopsis", "author", "published_date")
        # Allow for some more advanced filtering here
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'synopsis': ['exact', 'icontains'],
            'author': ['exact'],
            'author__name': ['exact', 'istartswith'],
        }
        interfaces = (graphene.relay.Node,)

    author_id: graphene.Field(lambda: Author)

    def resolve_author(self, info):
        return author_loader.load(self.author_id)


# Interfaces
class Animal(graphene.Interface):
    name = graphene.String(required=True)
    age = graphene.Int()


class CatType(graphene.ObjectType):
    class Meta:
        interfaces = (Animal,)

    breed = graphene.String(required=True)


# Unions
class SearchResultType(graphene.Union):
    class Meta:
        types = (AuthorNode, BookNode)