from django.contrib import admin
from .models import (
    Skill, ContactProfile, Certificate, Experience, MediaUrl
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('author', 'name')

@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(MediaUrl)
class MediaUrlAdmin(admin.ModelAdmin):
    list_display =('media_url', 'name', 'author')

