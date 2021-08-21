from django.contrib import admin
from .models import Faqs, GeneralSettings




class FaqsAdmin(admin.ModelAdmin):

    list_display = ['title']
    list_display_links=["title"]
    search_fields = ['title', 'desc']

    class Meta:
        model = Faqs

class GeneralSettingsAdmin(admin.ModelAdmin):


    def has_add_permission(self, request):
        record = GeneralSettings.objects.all()
        if len(record)!=0:
            return False
        else:
            return True

    class Meta:
        model = GeneralSettings



admin.site.register(Faqs,FaqsAdmin)
admin.site.register(GeneralSettings,GeneralSettingsAdmin)
