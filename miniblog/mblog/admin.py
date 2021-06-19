from django.contrib import admin
from .models import blogPost, Contact, Profile
# Register your models here.
@admin.register(blogPost)
class blogPostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'date']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','email', 'date']    

admin.site.register(Profile)    