﻿from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

import json
import urllib

# For orders_test only
from datetime import datetime
from django.template.loader import get_template
from pytz import timezone
import uuid
import requests

def home(request):
    return render(request,
                  template_name='home.html')


def search(request):
    return render(request,
                  template_name='search.html')


def photos(request):
    return render(request,
                  template_name='photos.html')


def orders_test(request):

    url = "https://preview.webservices.fujifilmesys.com/fes.digitalintegrationservices/order/orderservices.asmx"
    headers = {'content-type': 'text/xml; charset=utf-8', 'SOAPAction': 'FES.DigitalIntegrationServices/OrderSubmit'}

    body = ""

    c = dict()

    # General configuration for order
    c['AppKey'] = '4E9F-D562-637E-427F'
    c['FulfillerID'] = '30180'
    c['OriginatorName'] = 'SSI Ordering System'

    today = timezone('US/Pacific').localize(datetime.now()).strftime("%Y-%m-%dT%H:%M:%S%z")
    c['CheckoutDate'] = today
    c['CreateDate'] = today

    # Order ID information
    c['OriginatorSubOrderID'] = str(uuid.uuid4())[0:8]
    c['OriginatorOrderID'] = str(uuid.uuid4())[0:8]

    # User information
    c['OriginatorUserID'] = '23'
    c['FirstName'] = 'Aakash'
    c['LastName'] = 'Rayate'

    # Address information
    c['Address1'] = '1565 Jefferson Rd'
    c['Address2'] = 'Bldg 300'
    c['Address3'] = 'Suite 320'
    c['City'] = 'Rochester'
    c['State'] = 'NY'
    c['PostalCode'] = '14623'
    c['Country'] = 'US'
    c['Phone'] = '9033080477'
    c['Email'] = 'arayate@vavni.com'

    body = get_template('order_template.xml').render(c)

    print("#" * 30 + ' SOAP REQUEST ' + "#" * 30)

    #return HttpResponse(body, content_type='application/xml')
    response = requests.post(url, data=body, headers=headers)
    return HttpResponse(response.content, content_type='application/xml')


def products(request):
    print(request.META)
    selected_photos = list(json.loads(urllib.unquote(request.COOKIES.get('cashman.selected_photos')).decode('utf-8')))
    venue_id = request.COOKIES.get('venue_id')

    # Create new session for customer
    if selected_photos:
        s = functions.Session()

        user = s.create_user()
        s.import_images(selected_photos, venue_id)
    else:
        reverse('cashman_photos')



    return HttpResponse(selected_photos)
    return render(request,
                  template_name='edit.html')