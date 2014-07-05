import time

from django.shortcuts import render_to_response
from datetime import datetime
from sales_record.models import Sale

def display_results(request):
    base_datetime = datetime(2014,7,5,12,0,0)
    minutes = range(0,660,10)
    sales = [0 for m in minutes]
    all_sales = Sale.objects.all()

    for sale in all_sales:
        diff = time.mktime(sale.time.timetuple()) - time.mktime(base_datetime.timetuple())
        minute = int(diff / 600)
        if 0 < minute < 660:
            sales[minute] += 1
        else:
            sales[0] += 1

    total = sum(sales)

    scale = int(max(sales)/10)
    if scale == 0:
        scale = 1
    for sale in sales:
        sale = sale / scale

    return render_to_response('index.html', {'sales':sales, 'minutes':minutes, 'scale':scale, 'total':total},)
