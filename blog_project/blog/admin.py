from django.contrib import admin
from .models import Post, Comment


class CommentInLine(admin.StackedInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inLines = [
        CommentInLine,
    ]


admin.site.register(Post)
admin.site.register(Comment)


