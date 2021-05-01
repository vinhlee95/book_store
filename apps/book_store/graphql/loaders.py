from promise import Promise
from promise.dataloader import DataLoader

from apps.book_store.models import Author, Book


class AuthorLoader(DataLoader):
    def batch_load_fn(self, keys):
        # Here we return a promise that will result on the
        # corresponding user for each key in keys
        authors = {author.id: author for author in Author.objects.filter(id__in=keys)}
        results = [authors.get(author_id) for author_id in keys]
        return Promise.resolve(results)


class BookLoader(DataLoader):
    def batch_load_fn(self, keys):
        books = {author_id: [book for book in Book.objects.filter(author_id=author_id)] for author_id in keys}
        results = [books.get(author_id) for author_id in keys]
        return Promise.resolve(results)


author_loader = AuthorLoader()
book_loader = BookLoader()
