from django.contrib import admin

# Register your models here.

from .models import PostModel

from contact.models import ContactModel


class PostAdmin(admin.ModelAdmin):
    readonly_fields = [

        'slug',
        'publish',
        'update',
    ]


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(PostModel, PostAdmin)
