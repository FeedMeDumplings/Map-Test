from django.shortcuts import render, get_object_or_404, redirect
from .models import AreaLocation, GasStation, Rest, Store
# Create your views here.

def home(request):
	area_list = AreaLocation.objects.all()
	return render(request, 'map_app/home.html', { 'area_list' : area_list })

def area_search(request):
	if request.method == 'POST':
		search_id = request.POST.get('textfield', None)
		if search_id:
			s = get_object_or_404(AreaLocation, zip_code=search_id)
			if '_area' in request.POST:
					return render(request, 'map_app/area_search.html', { 'area' : s })
		else:
			if '_gas' in request.POST:
				filter_id = request.POST.get('_gas', None)
				if filter_id:
					s = get_object_or_404(AreaLocation, id = filter_id)
					return render(request, 'map_app/gas_station.html', { 'station' : s })
			elif '_rest' in request.POST:
				filter_id = request.POST.get('_rest', None)
				if filter_id:
					s = get_object_or_404(AreaLocation, id = filter_id)
					return render(request, 'map_app/rest.html', { 'rest' : s })
			elif '_store' in request.POST:
				filter_id = request.POST.get('_store', None)
				if filter_id:
					s = get_object_or_404(AreaLocation, id = filter_id)
					return render(request, 'map_app/store.html', { 'store' : s })		
	return redirect('home')