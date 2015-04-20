from django.contrib import admin
from .models import Presentation, Slide, OrderedSlides


class OrderedSlidesInline(admin.TabularInline):
    model = OrderedSlides
    extra = 1


class PresentationAdmin(admin.ModelAdmin):
    inlines = (OrderedSlidesInline, )


admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Slide)
