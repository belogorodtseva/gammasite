from django.contrib import admin

from gamma.models import Projects,Models,Services,News,Gallery,Image

admin.site.register(Models)
admin.site.register(Services)
admin.site.register(News)
admin.site.register(Gallery)

class ImageInline(admin.TabularInline):
    model = Image

class ProjectsAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Image)
