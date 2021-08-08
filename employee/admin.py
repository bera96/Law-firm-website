from django.contrib import admin
from .models import Employee, PracticeAreas, Certificate


class CertificateAdmin(admin.ModelAdmin):

    list_display = ['title']
    list_display_links=["title"]
    search_fields = ['title', 'desc']

    class Meta:
        model = Certificate





class AreasAdmin(admin.ModelAdmin):

    list_display = ['title']
    list_display_links=["title"]
    search_fields = ['title', 'desc']

    class Meta:
        model = PracticeAreas
        

class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['name', 'surname', 'faculty']
    exclude=('slug',)
    list_display_links=["name"]
    list_filter = ['faculty', 'areas']
    search_fields = ['name', 'surname', 'description' ,'faculty']
    #prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Employee



admin.site.register(Certificate,CertificateAdmin)
admin.site.register(PracticeAreas,AreasAdmin)
admin.site.register(Employee,EmployeeAdmin)