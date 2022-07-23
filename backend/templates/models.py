from django.core.validators import FileExtensionValidator
from django.db import models
from enums import League
from taggit.managers import TaggableManager


class Item(models.Model):
    image = models.ImageField(
        'изображение',
        validators=[FileExtensionValidator(['svg'])],
    )
    packs = models.ManyToManyField(
        'Pack',
        verbose_name='пак',
        related_name='items',
        blank=True,
    )
    tags = TaggableManager(
        verbose_name='теги',
        help_text='список тегов, разделенных запятыми',
        through=None,
        blank=True,
    )

    class Meta:
        verbose_name = 'элемент'
        verbose_name_plural = 'элементы'

    def __str__(self):
        return f'{self.id} {self.tags}'


class Pack(models.Model):
    class Colour(models.TextChoices):
        DARK = 'dark', 'темный'
        LIGHT = 'light', 'светлый'

    title = models.CharField(
        'название',
        max_length=40,
    )
    colour = models.CharField(
        'цвет',
        max_length=5,
        choices=Colour.choices,
    )
    tags = TaggableManager(
        verbose_name='теги',
        help_text='список тегов, разделенных запятыми',
        through=None,
        blank=True,
    )
    least_permitted_league = models.CharField(
        'наименьшая разрешенная лига',
        choices=League.choices,
        max_length=10,
    )
    width = models.PositiveIntegerField(
        'ширина',
    )
    heigth = models.PositiveIntegerField(
        'высота',
    )

    class Meta:
        verbose_name = 'пак'
        verbose_name_plural = 'паки'

    def __str__(self):
        return self.title


class Template(models.Model):
    preview = models.ImageField(
        'превью',
    )

    class Meta:
        verbose_name = 'шаблон'
        verbose_name_plural = 'шаблоны'

    def __str__(self):
        return f'Шаблон {self.id}'


class Part(models.Model):
    leftmost_coordinate = models.PositiveIntegerField(
        'координаты левой стороны',
    )
    uppermost_coordinate = models.PositiveIntegerField(
        'координаты верхней стороны',
    )
    rightmost_coordinate = models.PositiveIntegerField(
        'координаты правой стороны',
    )
    lowermost_coordinate = models.PositiveIntegerField(
        'координаты нижней стороны',
    )
    template = models.ForeignKey(
        'Template',
        verbose_name='шаблон',
        related_name='parts',
        on_delete=models.CASCADE,
    )
    pack = models.ForeignKey(
        'Pack',
        verbose_name='пак',
        related_name='parts',
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'часть шаблона'
        verbose_name_plural = 'части шаблона'

    def __str__(self):
        return f'Часть шаблона {self.id}'
