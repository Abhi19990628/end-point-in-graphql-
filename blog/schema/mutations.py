import graphene
from .node import PostType
from ..models import Author, Post

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        context = graphene.String(required=True)
        author_id = graphene.ID(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, context, author_id):
        try:
            author = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            raise Exception("Author with the given ID does not exist")

        post = Post(title=title, context=context, author=author)
        post.save()
        return CreatePost(post=post)

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        context = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, title=None, context=None):
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Exception("Post not found")

        if title is not None:
            post.title = title
        if context is not None:
            post.context = context

        post.save()
        return UpdatePost(post=post)

class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Exception("Post not found")

        post.delete()
        return DeletePost(success=True)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
