from django.contrib import admin
from learning_app.models import UserProfileModel, Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')
    list_filter = ('author', 'text')
    search_fields = ('text', 'author')

admin.site.register(UserProfileModel)
admin.site.register(Note, NoteAdmin)
