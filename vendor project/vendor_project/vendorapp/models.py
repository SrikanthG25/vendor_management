from django.db import models

STATUS = [('order','order'),('pending','pending'),('delivered','delivered')]

class Vendor(models.Model):
    name = models.CharField(max_length=125)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=75, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "vendor_detail"

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS,max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.po_number
    class Meta:
        db_table = "purchase_order"
    
class PerformanceRecord(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    class Meta:
        db_table = "performance_record"