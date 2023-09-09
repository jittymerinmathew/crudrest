from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Customer)
# admin.site.register(Product)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

admin.site.register(Customer, CustomerAdmin)



class ProductAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Product._meta.get_fields()]
  
admin.site.register(Product,ProductAdmin)