from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class ArticleAdminForm(forms.ModelForm):
    article_content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_lvl', 'user_money', 'user_clan')
    list_display_links = ('id', 'user', 'user_lvl', 'user_money', 'user_clan')
    search_fields = ('user',)

class ClanAdmin(admin.ModelAdmin):
    list_display = ('id', 'clan_name', 'clan_description', 'clan_is_open')
    list_display_links = ('id', 'clan_name', 'clan_description', 'clan_is_open')
    search_fields = ('clan_name',)

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('id', 'article_title', 'article_created_at', 'article_photo')
    list_display_links = ('id', 'article_title', 'article_created_at', 'article_photo')
    search_fields = ('article_title',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Clan, ClanAdmin)
admin.site.register(Article, ArticleAdmin)

admin.site.site_title = 'Color Loss management'
admin.site.site_header = 'Color Loss management'