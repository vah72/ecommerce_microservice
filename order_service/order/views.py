from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Order
import requests

@csrf_exempt
def getAllOrder(request) :
    resp = {}
    data = []
    if request.method == 'GET':
        list_order = Order.objects.all()
        for order in list_order.values():
            data.append(order)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
    return HttpResponse(json.dumps(resp, default=str), content_type='application/json')

@csrf_exempt
def create_order(request):
    print("Yes")
    uname = request.POST.get("User Name")
    pro_id = request.POST.get("Product Id")
    total =  request.POST.get("Total")
    shipment_id = request.POST.get("Shipment Id")
    resp = {}
    if uname and pro_id and total and shipment_id:
        order = Order(username=uname, product_id=pro_id, total=total, shipment_id=shipment_id)
        if order:
            if checkProduct(pro_id):
                order.save()
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Create a new order successfully'
            else :
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = f"There is no product {pro_id}"
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Data is invalid'
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp), content_type='application/json')

def checkProduct(id):
    url = 'http://127.0.0.1:8001/get_product_data/'
    listProduct = requests.get(url).json()
    for product in listProduct['data']:
        if product['product_id'] == id:
            return True
    return False

def orderSuccess(request, order_id):
    resp = {}
    if request.method == 'DELETE':
        order = Order.objects.get(pk=order_id)
        print(order)
        order.delete()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Update order successfully'
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Update order unsuccessfully'
    return HttpResponse(json.dumps(resp), content_type='application/json')

def getOrderDetail(request, order_id):
    resp = {}
    data = []
    if request.method == 'GET':
        orders = Order.objects.filter(pk=order_id)
        for order in orders.values():
            order
        if order:
            data.append(order)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
        else :
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Error'
    return HttpResponse(json.dumps(resp, default=str), content_type='application/json')



