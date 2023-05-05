import re

from rest_framework import serializers


def validate_username(value):
    if not re.search(r'^[\w.@+-]+$', value):
        raise serializers.ValidationError(
            'Ошибка шаблона'
        )
    if value.lower() == 'me':
        raise serializers.ValidationError(
            'Имя пользователя необходимо изменить!'
        )
    return value
