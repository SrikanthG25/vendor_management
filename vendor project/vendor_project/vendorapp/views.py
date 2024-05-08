from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
import logging

logger = logging.getLogger(__name__)

class vendorView(generics.GenericAPIView):
    def post(self,request):
        try:
            data = request.data
            name = data.get("name")
            contact_details = data.get("contact_details")
            address = data.get("address")
            vendor_code = data.get("vendor_code")
            on_time_delivery_rate = data.get("on_time_delivery_rate")
            quality_rating_avg = data.get("quality_rating_avg")
            average_response_time = data.get("average_response_time")
            fulfillment_rate = data.get("fulfillment_rate")

            if not name:
                return Response({"status":400,"message":"please give name"})
            if not vendor_code:
                return Response({"status":400,"message":"please give vendor code"})
            
            create_data = {
                "name" : name,
                "contact_details" : contact_details,
                "address" : address,
                "vendor_code" : vendor_code,
                "on_time_delivery_rate" : on_time_delivery_rate,
                "quality_rating_avg" : quality_rating_avg,
                "average_response_time" : average_response_time,
                "fulfillment_rate" : fulfillment_rate
            }
            Vendor.objects.create(**create_data)
            return Response({'status': 'success','message':'Successfully Added'} , status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong Please try again'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request):
        try:
            data = request.data
            vendor_id = data.get('vendor_id')
            
            if not vendor_id:
                return Response({"status":400,"message":"please give vendor id"})
            vendor_data = Vendor.objects.get(id = vendor_id)
            vendor_data.name = data.get("name")
            vendor_data.contact_details = data.get("contact_details")
            vendor_data.address = data.get("address")
            vendor_data.vendor_code = data.get("vendor_code")
            vendor_data.on_time_delivery_rate = data.get("on_time_delivery_rate")
            vendor_data.quality_rating_avg = data.get("quality_rating_avg")
            vendor_data.average_response_time = data.get("average_response_time")
            vendor_data.fulfillment_rate = data.get("fulfillment_rate")
            vendor_data.save()
            return Response({'status': 'success','message':'Vendor updated successfully!'} , status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong Please try again'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self,reauest):
        try:
            data = reauest.GET
            vendor_id = data.get('vendor_id')
            if vendor_id:
                vendor_data = Vendor.objects.filter(id=vendor_id,is_active=False).values('id','name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')
                return Response({'status': 'success','message':'Vendor Details','data' : vendor_data} , status=status.HTTP_200_OK)
            else:
                vendor_data = Vendor.objects.filter(is_active=False).values('id','name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')
                return Response({'status': 'success','message':'Vendor Details','data' : vendor_data} , status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong Please try again'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request):
        try:
            data = request.GET
            vendor_id = data.get('vendor_id')
            if not vendor_id:
                return Response({"status":400,"message":"please give vendor id"})
            del_data =  Vendor.objects.get(id=vendor_id,is_active=False)
            del_data.is_active = True
            del_data.save()
            return Response ({"status":200,"message":"deleted succesfully"})
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 'fail', 'message': 'Something went wrong Please try again'} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PurchaseOrderView(generics.GenericAPIView):
    def post(self, request):
        try:
            data = request.data
            po_number = data.get("po_number")
            vendor_id = data.get("vendor_id")
            order_date = data.get("order_date")
            delivery_date = data.get("delivery_date")
            items = data.get("items")
            quantity = data.get("quantity")
            status = data.get("status")
            quality_rating = data.get("quality_rating")
            issue_date = data.get("issue_date")
            acknowledgment_date = data.get("acknowledgment_date")
            print(vendor_id)

            if not po_number:
                return Response({"status": 400, "message": "Please provide a PO number"})
            if not vendor_id:
                return Response({"status": 400, "message": "Please provide vendor details"})

            create_data = {
                "po_number": po_number,
                "vendor_id": vendor_id,
                "order_date": order_date,
                "delivery_date": delivery_date,
                "items": items,
                "quantity": quantity,
                "status": status,
                "quality_rating": quality_rating,
                "issue_date": issue_date,
                "acknowledgment_date": acknowledgment_date,
            }
            PurchaseOrder.objects.create(**create_data)
            return Response({'status': 200, 'message': 'Successfully Added'})
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 500, 'message': 'Something went wrong. Please try again'})
        
    def put(self,request):
        try:
            data = request.data
            po_id = data.get('po_id')
            
            if not po_id:
                return Response({"status":400,"message":"please give vendor id"})
            vendor_data = PurchaseOrder.objects.get(id = po_id)
            vendor_data.po_number = data.get("po_number")
            vendor_data.vendor_id = data.get("vendor_id")
            vendor_data.order_date = data.get("order_date")
            vendor_data.delivery_date = data.get("delivery_date")
            vendor_data.items = data.get("items")
            vendor_data.quantity = data.get("quantity")
            vendor_data.status = data.get("status")
            vendor_data.quality_rating = data.get("quality_rating")
            vendor_data.issue_date = data.get("issue_date")
            vendor_data.acknowledgment_date = data.get("acknowledgment_date")
            vendor_data.save()
            return Response({'status': 200,'message':'Purchase Order updated successfully!'} , status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 500, 'message': 'Something went wrong Please try again'})
        
    def get(self,reauest):
        try:
            data = reauest.GET
            po_id = data.get('po_id')
            if po_id:
                purchase_order = PurchaseOrder.objects.filter(id=po_id,is_active=False).values('id','po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date')
                return Response({'status': 200,'message':'Purchase Order Details','data' : purchase_order} , status=status.HTTP_200_OK)
            else:
                purchase_order = PurchaseOrder.objects.filter(is_active=False).values('id','po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date')
                return Response({'status': 200,'message':'Purchase Order Details','data' : purchase_order} , status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 500, 'message': 'Something went wrong Please try again'})
        
    def delete(self,request):
        try:
            data = request.GET
            po_id = data.get('po_id')
            if not po_id:
                return Response({"status":400,"message":"please give vendor id"})
            del_data =  PurchaseOrder.objects.get(id=po_id,is_active=False)
            print(del_data)
            del_data.is_active = True
            del_data.save()
            return Response ({"status":200,"message":"deleted succesfully"})
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 500, 'message': 'Something went wrong Please try again'})
        
class PerformanceRecordView(generics.GenericAPIView):     
    def get(self,reauest):
        try:
            data = reauest.GET
            vendor_id = data.get('vendor_id')
            if vendor_id:
                purchase_order = PerformanceRecord.objects.filter(vendor_id=vendor_id).values('vendor_id','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')
                return Response({'status': 200,'message':'Purchase Order Details','data' : purchase_order} , status=status.HTTP_200_OK)
            else:
                purchase_order = PerformanceRecord.objects.values('vendor_id','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')
                return Response({'status': 200,'message':'Purchase Order Details','data' : purchase_order} , status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Exception {}'.format(e.args))
            return Response({'status': 500, 'message': 'Something went wrong Please try again'})
