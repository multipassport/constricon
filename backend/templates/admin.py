from django.contrib import admin
from templates.models import Item, Pack, Part, Template


class ItemInline(admin.TabularInline):
    model = Item.packs.through
    verbose_name = 'элемент'
    verbose_name_plural = 'элементы'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


class PartInline(admin.TabularInline):
    model = Part


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    inlines = [PartInline]
