from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_lvl', 'user_money', 'user_clan')
    list_display_links = ('id', 'user', 'user_lvl', 'user_money', 'user_clan')
    search_fields = ('user',)

class ClanAdmin(admin.ModelAdmin):
    list_display = ('id', 'clan_name', 'clan_description', 'clan_is_open')
    list_display_links = ('id', 'clan_name', 'clan_description', 'clan_is_open')
    search_fields = ('clan_name',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Clan, ClanAdmin)

admin.site.site_title = 'Color Loss management'
admin.site.site_header = 'Color Loss management'