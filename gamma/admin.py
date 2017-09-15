from django.contrib import admin

from gamma.models import Projects,Models,Services,News,Gallery,Image,ServicesSecond

admin.site.register(Models)

admin.site.register(News)
admin.site.register(Gallery)

class ImageInline(admin.TabularInline):
    model = Image

class ProjectsAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

class ServicesSecondInline(admin.TabularInline):
    model = ServicesSecond

class ServicesAdmin(admin.ModelAdmin):
    inlines = [
        ServicesSecondInline,
    ]

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Image)

admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesSecond)
