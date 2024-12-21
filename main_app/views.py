import json

from django.db.models.expressions import result
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def trigger(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0715447860'
    amount = 1
    account_reference = '001-thisbelarry'
    transaction_desc = 'Crowdy'
    callback_url = 'https://14f1-149-40-62-22.ngrok-free.app/callback'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

@csrf_exempt
def callback(request):
    response = json.loads(request.body)
    print(response)
    return HttpResponse('OK')

# extract and save the details in  in db