from .models import *
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductAdminForm(forms.ModelForm):
    About = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Basket)


