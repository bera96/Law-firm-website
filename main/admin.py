from django.contrib import admin
from .models import Faqs




class FaqsAdmin(admin.ModelAdmin):

    list_display = ['title']
    list_display_links=["title"]
    search_fields = ['title', 'desc']

    class Meta:
        model = Faqs



admin.site.register(Faqs,FaqsAdmin)