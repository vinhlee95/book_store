from promise import Promise
from promise.dataloader import DataLoader

from apps.book_store.models import Author


class AuthorLoader(DataLoader):
    def batch_load_fn(self, keys):
        # Here we return a promise that will result on the
        # corresponding user for each key in keys
        authors = {author.id: author for author in Author.objects.filter(id__in=keys)}
        return Promise.resolve([authors.get(author_id) for author_id in keys])


author_loader = AuthorLoader()
