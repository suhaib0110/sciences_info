from django.contrib import admin
from .models import (
    Report, Author, Rock, Mineral, FAQ
    )

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

admin.site.register(Report)

@admin.register(Rock)
class RockAdmin(admin.ModelAdmin):
    list_display = ('name', 'rock_type', 'author')

@admin.register(Mineral)
class MineralAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'author')