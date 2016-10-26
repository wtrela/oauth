from django.contrib import admin
from oauth.models.profile import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass