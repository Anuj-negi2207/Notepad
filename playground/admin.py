from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Note

class ProfileInline(admin.StackedInline):
    model = Profile

class NoteInline(admin.StackedInline):
    model = Note

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline, NoteInline]




admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
#admin.site.register(Profile)