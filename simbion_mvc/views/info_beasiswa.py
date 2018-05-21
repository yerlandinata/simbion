from django.shortcuts import render
from simbion_mvc.entity import skema_beasiswa_aktif
from simbion_mvc.dao import skema_beasiswa_aktif_dao  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

response = {}
def info_beasiswa(request,):
    beasiswa_list_all = skema_beasiswa_aktif_dao.getall()
    #ToDo IMPLEMENT METHOD TO GET BEASISWA LIST
    
    page = request.GET.get('page',1)
    paginate_data = paginate_page(page,beasiswa_list_all)
    beasiswa_list = paginate_data['data']
    page_range = paginate_data['page_range']
    
    response['beasiswa_list'] = beasiswa_list
    response['page_range'] = page_range
    return render(request, '4_info_beasiswa/index.html',response)

def paginate_page(page, data_list):
	paginator = Paginator(data_list, 10)
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)

	start_index = data.start_index()
	end_index = data.end_index()

	page_range = list(paginator.page_range)[start_index:end_index]
	paginate_data = {'data':data, 'page_range':page_range}
	return paginate_data

