from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/', vendorView.as_view()),
    path('purchase_order/', PurchaseOrderView.as_view()),
    path('vendors/{vendor_id}/performance:', PerformanceRecordView.as_view()),
]