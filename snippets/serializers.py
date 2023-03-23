from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Post, Comments


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["user", "title", "body", "created", "updated"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["user", "post", "body", "created", "updated"]
