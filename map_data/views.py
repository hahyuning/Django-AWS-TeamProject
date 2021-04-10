from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request

from map_data.models import Map_info, Map_data


def Map(request):
    return render(request , 'map_data/map.html')

#주제별
def Museum(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='박물관합계')
    print(info_datas)
    return render(request, 'map_data/culture/map_data_Culture.html',{'test': datas,'data' : info_datas})

def Concert_hall(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='공연장합계')
    print(info_datas)
    return render(request, 'map_data/culture/map_data_Culture.html', {'test': datas, 'data': info_datas})

def Kindergarden(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='유치원 학교수')
    print(info_datas)
    return render(request, 'map_data/education/map_data_Education.html', {'test': datas, 'data': info_datas})

def Elementary(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='초등학교 학교수')
    print(info_datas)
    return render(request, 'map_data/education/map_data_Education.html', {'test': datas, 'data': info_datas})

def Middle(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='중학교 학교수')
    print(info_datas)
    return render(request, 'map_data/education/map_data_Education.html', {'test': datas, 'data': info_datas})

def High(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='고등학교 학교수')
    print(info_datas)
    return render(request, 'map_data/education/map_data_Education.html', {'test': datas, 'data': info_datas})

def General_hospital(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='종합병원 개수')
    print(info_datas)
    return render(request, 'map_data/health_welfare/map_data_Health_welfare.html', {'test': datas, 'data': info_datas})

def Hospital(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='의원 개수')
    print(info_datas)
    return render(request, 'map_data/health_welfare/map_data_Health_welfare.html', {'test': datas, 'data': info_datas})

def Pharmacy(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='약국 합계')
    print(info_datas)
    return render(request, 'map_data/health_welfare/map_data_Health_welfare.html', {'test': datas, 'data': info_datas})

def Dentist(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='치과병원')
    print(info_datas)
    return render(request, 'map_data/health_welfare/map_data_Health_welfare.html', {'test': datas, 'data': info_datas})

def Total_hospital(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='병원합계')
    print(info_datas)
    return render(request, 'map_data/health_welfare/map_data_Health_welfare.html', {'test': datas, 'data': info_datas})

def Library(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='도서관 합계')
    print(info_datas)
    return render(request, 'map_data/facility/map_data_Facility.html', {'test': datas, 'data': info_datas})

def Theaters(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='영화관 개수')
    print(info_datas)
    return render(request, 'map_data/facility/map_data_Facility.html', {'test': datas, 'data': info_datas})

def Sports_facility(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='체육시설 합계')
    print(info_datas)
    return render(request, 'map_data/facility/map_data_Facility.html', {'test': datas, 'data': info_datas})

def Park(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='공원 수')
    print(info_datas)
    return render(request, 'map_data/facility/map_data_Facility.html', {'test': datas, 'data': info_datas})

def Garbage_discharge(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='쓰레기 배출량')
    unit = '톤'
    print(info_datas)
    return render(request, 'map_data/environment/map_data_Environment.html', {'u':unit,'test': datas, 'data': info_datas})

def Satisfaction_with_using_green_space(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='녹지 이용 만족도')
    unit = '점 / 10점'
    print(info_datas)
    return render(request, 'map_data/environment/map_data_Environment.html', {'u':unit,'test': datas, 'data': info_datas})

def Fine_dust(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='미세먼지(㎍/㎥)')
    unit = '㎍/㎥'
    print(info_datas)
    return render(request, 'map_data/environment/map_data_Environment.html', {'u':unit,'test': datas, 'data': info_datas})

def Environmental_complaints(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='환경 관련 민원 수')
    unit = '건'
    print(info_datas)
    return render(request, 'map_data/environment/map_data_Environment.html', {'u':unit,'test': datas, 'data': info_datas})

def Noise_related_complaints(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='소음 관련 민원 수')
    unit = '건'
    print(info_datas)
    return render(request, 'map_data/environment/map_data_Environment.html', {'u':unit,'test': datas, 'data': info_datas})

def Number_of_registered_cars(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='등록 자동차 수')
    unit = '대'
    print(info_datas)
    return render(request, 'map_data/traffic/map_data_Traffic.html', {'u':unit,'test': datas, 'data': info_datas})

def Number_of_parking(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='주차장 수')
    unit = '곳'
    print(info_datas)
    return render(request, 'map_data/traffic/map_data_Traffic.html', {'u':unit,'test': datas, 'data': info_datas})

def Bus_satisfaction(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='버스 만족도')
    unit = '점 / 10점'
    print(info_datas)
    return render(request, 'map_data/traffic/map_data_Traffic.html', {'u':unit,'test': datas, 'data': info_datas})

def Subway_satisfaction(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='지하철 만족도')
    unit = '점 / 10점'
    print(info_datas)
    return render(request, 'map_data/traffic/map_data_Traffic.html', {'u':unit,'test': datas, 'data': info_datas})

def Taxi_satisfaction(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='택시 만족도')
    unit = '점 / 10점'
    print(info_datas)
    return render(request, 'map_data/traffic/map_data_Traffic.html', {'u':unit,'test': datas, 'data': info_datas})


def Theme(request):
    topic = request.GET['topic']
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme=topic)
    print(info_datas)
    return render(request, 'map_data/map_data.html', {'test': datas, 'data': info_datas})

def Culture(request):
    datas = Map_info.objects.all()
    return render(request, 'map_data/culture/map_Culture.html', {'test': datas})

def Health_welfare(request):
    datas = Map_info.objects.all()
    return render(request, 'map_data/health_welfare/map_Health_welfare.html', {'test': datas})

def Facility(request):
    datas = Map_info.objects.all()
    return render(request, 'map_data/facility/map_Facility.html', {'test': datas})

def Education(request):
    datas = Map_info.objects.all()
    return render(request, 'map_data/education/map_Education.html', {'test': datas})

def Population(request):
    datas = Map_info.objects.all()
    info_datas = Map_data.objects.filter(theme='인구수')
    print(info_datas)
    return render(request, 'map_data/population/map_Population.html', {'test': datas, 'data': info_datas})

def Traffic(request):
    datas = Map_info.objects.all()
    return render(request, 'map_data/traffic/map_Traffic.html', {'test': datas})

def Environment(request):
    datas = Map_info.objects.all()
    return render(request, 'map_data/environment/map_Environment.html', {'test': datas})
