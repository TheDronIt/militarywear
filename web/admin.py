from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _
from .models import *


class ProductAdmin(admin.ModelAdmin):
	filter_horizonal = ('Images',)

admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Tag)
admin.site.register(Size)

admin.site.register(Basket)
