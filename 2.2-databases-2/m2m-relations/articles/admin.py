from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_tags = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                count_tags += 1

        if count_tags == 0:
            raise ValidationError('Укажите основной раздел')
        if count_tags > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

