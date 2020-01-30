from django.contrib import admin
from .models import sale

# Register your models here.
class  saleModel1(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model= sale
admin.site.register(sale, saleModel1)