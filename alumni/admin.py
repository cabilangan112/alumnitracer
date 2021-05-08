from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Index, Thumbnail, Parallax, PersonalInformation,Department

# Register your models here.

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Index)
admin.site.register(Thumbnail)
admin.site.register(Parallax)
admin.site.register(PersonalInformation)