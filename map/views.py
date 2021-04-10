from django.shortcuts import render
from django.views.generic import ListView, DetailView
from map.models import Event
from django.db.models import Q

class Start(ListView):
    model = Event
    paginate_by = 10

class Detail(DetailView):
    model = Event
    template_name = 'map/event_detail.html'

def list_filter(request):
    filt_val = request.GET.get('filt')
    gu_val = request.GET.get('gu')
    if gu_val == "all":
        if filt_val != None:
            if filt_val == "공연":
                rows = Event.objects.filter(Q(classification="콘서트") | Q(classification="뮤지컬/오페라")
                       | Q(classification="연극") | Q(classification="국악") | Q(classification="클래식")
                       | Q(classification="무용") | Q(classification="독주/독창회"))
            elif filt_val == "전시":
                rows = Event.objects.filter(classification="전시/미술")
            elif filt_val == "축제":
                rows = Event.objects.filter(Q(classification="축제-시만화합") | Q(classification="축제-문화·예술")
                                            | Q(classification="축제-자연·경관") | Q(classification="축제-전통·역사"))
            elif filt_val == "교육/체험":
                rows = Event.objects.filter(classification="문화교양/강좌")
            elif filt_val == "기타":
                rows = Event.objects.filter(classification="기타")
            else: rows = Event.objects.all()
        else: rows = Event.objects.all()
    else:
        if filt_val != None:
            if filt_val == "공연":
                rows = Event.objects.filter(Q(gu=gu_val) & (Q(classification="콘서트") | Q(classification="뮤지컬/오페라")
                       | Q(classification="연극") | Q(classification="국악") | Q(classification="클래식")
                       | Q(classification="무용") | Q(classification="독주/독창회")))
            elif filt_val == "전시":
                rows = Event.objects.filter(Q(gu=gu_val) & Q(classification="전시/미술"))
            elif filt_val == "축제":
                rows = Event.objects.filter(Q(gu=gu_val) & (Q(classification="축제-시만화합") | Q(classification="축제-문화·예술")
                                            | Q(classification="축제-자연·경관") | Q(classification="축제-전통·역사")))
            elif filt_val == "교육/체험":
                rows = Event.objects.filter(Q(gu=gu_val) & Q(classification="문화교양/강좌"))
            elif filt_val == "기타":
                rows = Event.objects.filter(Q(gu=gu_val) & Q(classification="기타"))
            else: rows = Event.objects.filter(gu=gu_val)
        else: rows = Event.objects.filter(gu=gu_val)
    return render(request, "map/event_filt.html", {"event": rows, "gu_l": gu_val, "filt_v": filt_val})

