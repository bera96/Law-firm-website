from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'published_date']
    exclude=('slug',)
    list_display_links=["title"]
    list_filter = ['published_date']
    search_fields = ['title', 'content']
    #prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Post



admin.site.register(Post,PostAdmin)
