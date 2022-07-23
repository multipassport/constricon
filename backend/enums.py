from django.db.models import IntegerChoices


class League(IntegerChoices):
    FIRST = 1, 'Первая лига'
    SECOND = 2, 'Вторая лига'
    THIRD = 3, 'Третья лига'
