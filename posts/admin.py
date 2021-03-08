from django.contrib import admin

# Register your models here.
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке,
    # добавили primary key (pk) в качестве поля в list_display
    list_display = ('pk', 'text', 'pub_date', 'author')
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # фильтрация по полю:
    list_filter = ("pub_date",)
    # это свойство сработает для всех колонок:
    # где пусто - там будет эта строка
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    search_field = ('title')
    # list_filter = ('title',)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
