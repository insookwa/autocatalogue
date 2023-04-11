from django.contrib import admin
from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Model)
class ModelsAdmin(admin.ModelAdmin):
    pass

@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    pass