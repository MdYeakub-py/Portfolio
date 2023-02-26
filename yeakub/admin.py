from django.contrib import admin
from .models import InfoDetails, Education, Services, Protfolio, AdminContact
# Register your models here.

admin.site.register(InfoDetails)
admin.site.register(Education)
admin.site.register(Services)
admin.site.register(Protfolio)
admin.site.register(AdminContact)

class Protfolio(admin.ModelAdmin):
    list_display= ('id', 'title', 'images')