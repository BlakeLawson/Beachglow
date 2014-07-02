from django.shortcuts import render_to_response
from chartit import DataPool, Chart
from sales_record.models import Sale

def display_results(request):
	# Filter 
	#saleObjects = Sale.objects.all()

	

	data = DataPool(series=[{
		'options': {'source': Sale.objects.all()},
		'terms': ['product', 'time']
	}])

	chart = Chart(
		datasource=data,
		series_options=[{
			'options':{
				'type':'line',
				'stacking':False},
			'terms':{
				'product':['time',],}
		}],
		chart_options={
			'title':{'text':'Inventory Sold vs Time Sold'},
			'xAxis':{
				'title':{
					'text':'Time of Sale'}}
	})

	return render_to_response('index.html', {'chart':chart},)