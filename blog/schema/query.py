import graphene
from .node import PostType, AuthorType
from ..models import Post, Author

class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    authors = graphene.List(AuthorType)

    def resolve_posts(self, info):
        return Post.objects.all()

    def resolve_authors(self, info):
        return Author.objects.all()
