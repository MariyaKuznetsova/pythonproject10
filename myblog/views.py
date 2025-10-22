from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from myblog.models import Record


class RecordCreateView(CreateView):
    model = Record
    fields = ["title", "contents", "image", "is_publication", "number_of_views"]
    success_url = reverse_lazy("myblog:record_list")


class RecordDetailView(DetailView):
    model = Record

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class RecordListView(ListView):
    model = Record

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_publication=True)


class RecordUpdateView(UpdateView):
    model = Record
    fields = ["title", "contents", "image", "is_publication", "number_of_views"]
    success_url = reverse_lazy("myblog:record_list")

    def get_success_url(self):
        return reverse("myblog:record_detail", args=[self.kwargs.get("pk")])


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy("myblog:record_list")
