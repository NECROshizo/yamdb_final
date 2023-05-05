from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from reviews.models import Category, Genre, Title, Review, Comment


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""

    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для жанров"""

    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleGETSerializer(serializers.ModelSerializer):
    """Сериализатор - список произведений для чтения"""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')

    def get_rating(self, obj):
        """Получение среднего рейтинга, при отсутствие None"""
        rating = obj.reviews.aggregate(Avg('score')).get('score__avg')
        if rating:
            return round(rating)


class TitleEditSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и редактирования произведений"""
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description',
                  'genre', 'category')
        validators = [
            UniqueTogetherValidator(
                queryset=Title.objects.all(),
                fields=('name', 'year'),
                message='Это произведение уже добавлено в базу.'
            )
        ]


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзывов"""
    author = SlugRelatedField(slug_field='username', read_only=True,)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, data):
        """Проверка, что отзыв единственный на произведение"""
        request = self.context['request']
        author = request.user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)

        method_is_post = request.method == 'POST'
        review_exists = title.reviews.filter(author=author).exists()

        if method_is_post and review_exists:
            raise serializers.ValidationError('Отзыв уже написан')
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев к отзыву"""
    author = SlugRelatedField(slug_field='username', read_only=True,)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
