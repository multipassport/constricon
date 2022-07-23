from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager


class Icon(models.Model):
    preview = models.ImageField(
        'превью',
    )

    template = models.ForeignKey(
        'templates.Template',
        verbose_name='шаблон',
        related_name='icons',
        on_delete=models.PROTECT,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='пользователь',
        related_name='icons',
        on_delete=models.CASCADE,
    )

    tags = TaggableManager(
        verbose_name='теги',
        help_text='список тегов, разделенных запятыми',
        through=None,
        blank=True,
    )

    class Meta:
        verbose_name = 'иконка'
        verbose_name_plural = 'иконки'

    def __str__(self):
        return f'Иконка {self.id}'


class IconPart(models.Model):
    icon = models.ForeignKey(
        'Icon',
        verbose_name='иконка',
        related_name='part_items',
        on_delete=models.CASCADE,
    )
    part = models.ForeignKey(
        'templates.Part',
        verbose_name='часть шаблона',
        related_name='part_items',
        on_delete=models.PROTECT,
    )
    item = models.ForeignKey(
        'templates.Item',
        verbose_name='элемент',
        related_name='part_items',
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'часть иконки'
        verbose_name_plural = 'части иконки'

    def __str__(self):
        return f'Часть иконки {self.id}'
