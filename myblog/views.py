from myblog.models import Record
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

class RecordCreateView(CreateView):
    model = Record
    fields = ['title', 'contents', 'is_publication', 'number_of_views', 'created_at']
    success_url = reverse_lazy('myblog:record_list')


class RecordDetailView(DetailView):
    model = Record


class RecordListView(ListView):
    model = Record


class RecordUpdateView(UpdateView):
    model = Record
    fields = ['title', 'contents', 'is_publication', 'number_of_views', 'created_at']
    success_url = reverse_lazy('myblog:record_list')


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('myblog:record_list')

