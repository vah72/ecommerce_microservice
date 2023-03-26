from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details


@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
        if data:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
def getProdata(id):
    products = product_details.objects.filter(product_id=id)
    for p in products.values():
        return p
@csrf_exempt
def getProductByID(request, proid):
    data = {}
    resp = {}
    # This will fetch the data from the database.
    prodata = getProdata(proid)
    if prodata:
        # data["Product id"] = prodata.get("product_id","");
        #  product_id = models.CharField(max_length=10)
        #     product_category = models.CharField(max_length=50)
        #     product_name = models.CharField(max_length=100)
        #     availability = models.CharField(max_length=15)
        #     price
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = prodata
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')