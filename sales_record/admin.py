from django.contrib import admin
from sales_record.models import Sale

class SaleAdmin(admin.ModelAdmin):
    list_display = ['product','time']
    list_filter = ['time','product']

admin.site.register(Sale)
