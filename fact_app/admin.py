from django.contrib import admin

from.models import Customer, Invoice, Article




class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'sex', 'age', 'city', 'zip_code')

# Register your models here.
class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer', 'invoice_date_time', 'total', 'last_update_date', 'paid', 'invoice_type', 'comments')

class AdminArticle(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'quantity', 'unit_price', 'total')

admin.site.register(Customer, AdminCustomer)

admin.site.register(Invoice, AdminInvoice)

admin.site.register(Article , AdminArticle) 
