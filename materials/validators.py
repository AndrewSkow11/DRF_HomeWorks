from rest_framework.serializers import ValidationError

allowed_resource = 'youtube.com'


def validate_url_resource(value):
    if allowed_resource not in value:
        raise ValidationError("Разрешены ссылки только на youtube.com")
