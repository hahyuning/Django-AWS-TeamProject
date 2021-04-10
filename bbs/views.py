from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from bbs.models import Bbs

class SelectAll(ListView):
    model = Bbs
    paginate_by = 10

class Detail(DetailView):
    model = Bbs
    template_name = 'bbs/detail.html'

class Create(CreateView):
    model = Bbs
    fields = ['title', 'content', 'writer']
    template_name_suffix = '_create'
    success_url = reverse_lazy('bbs:selectAll')

def delete(request):
    if 'id' in request.GET:
        contents = get_object_or_404(Bbs, pk=request.GET.get('id'))
        contents.delete()
    return HttpResponseRedirect('selectAll')

class Update(UpdateView):
    model = Bbs
    fields = ['title', 'content']
    template_name = 'bbs/bbs_update.html'
    success_url = reverse_lazy('bbs:selectAll')

    # def dispatch(self, request, *args, **kwargs):
    #     object = self.get_object()
    #     if object.writer != request.user:
    #         messages.warning(request, '수정할 권한이 없습니다.')
    #         return HttpResponseRedirect('bbs:selectAll')
    #     else:
    #         return super(Update, self).dispatch(request, *args, **kwargs)
