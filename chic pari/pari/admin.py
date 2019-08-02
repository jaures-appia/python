from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'prenom', 'email')
    list_filter    = ('email', 'telephone',)
    date_hierarchy = 'date_inscription'
    ordering       = ('date_inscription', )
    search_fields  = ('email', 'telephone')

admin.site.register(Client, ClientAdmin)

# Register your models here.
