from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    GENDER = (       
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    sex = models.CharField(max_length=1, choices=GENDER)
    age = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='customers')  # cette facture est enregistre par user 

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name

class Invoice(models.Model):
    INVOICE_TYPES = (
        ('F', 'Facture'),
        ('C', 'Credit'),
        ('A', 'Avoir'),
        ('P', 'Proforma'),
        ('R', 'Recus'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)
    invoice_date_time = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10000, decimal_places=2)
    last_update_date = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPES, default='F')
    comments = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return f"{self.customer.name}_{self.invoice_date_time}"

    @property
    def get_total(self):
        articles = self.article_set.all()
        total = sum(article.get_total for article in articles)
        return total

class Article(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10000, decimal_places=2)
    total = models.DecimalField(max_digits=10000, decimal_places=2)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    @property
    def get_total(self):
        return self.quantity * self.unit_price