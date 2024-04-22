# Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.
# То есть ссылки на видео можно прикреплять в материалы, а ссылки на сторонние образовательные платформы или личные сайты — нельзя.


# Создайте отдельный файл
# validators.py
# , реализуйте валидатор, проверяющий ссылку, которую пользователь хочет записать в поле урока с помощью класса или функции.
# Интегрируйте валидатор в сериализатор.
# Если вы используете функцию-валидатор — указанием валидаторов для поля сериализатора
# validators=[ваш_валидатор]
# .
# Если вы используете класс-валидатор — указанием валидаторов в
# class Meta
# :
# validators = [ваш_валидатор(field='поле_которое_валидируем')]
# .

import re

from rest_framework.serializers import ValidationError

allowed_resource = 'youtube.com/watch'


def validate_url_resource(value):
    if allowed_resource not in value:
        raise ValidationError("Разрешены ссылки только на youtube.com")

# class VideoValidator:
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#
#         # проверка допустимости ссылки (только на youtube)
#         # reg = re.compile('youtube.com')
#         # tmp_val = dict(value).get(self.field)
#         #
#         # if bool(reg.match(tmp_val)):
#         #     raise ValueError("Указана ссылка на сторонний ресурс"
#         #                      "\nРазрешён только youtube.com")
#
#         # if 'youtube.com' not in value:
#         #     raise ValueError("Указана ссылка на сторонний ресурс"
#         #                          "\nРазрешён только youtube.com")
