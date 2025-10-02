from django.urls import path
from myblog.apps import MyblogConfig
from myblog.views import RecordListView, RecordDetailView, RecordCreateView, RecordUpdateView, RecordDeleteView

app_name = MyblogConfig.name

urlpatterns = [
    path('myblog/', RecordListView.as_view(), name='record_list'),
    path("myblog/<int:pk>/", RecordDetailView.as_view(), name="record_detail"),
    path("myblog/create/", RecordCreateView.as_view(), name="record_create"),
    path("myblog/<int:pk>/update/", RecordUpdateView.as_view(), name="record_update"),
    path("myblog/<int:pk>/delete/", RecordDeleteView.as_view(), name="record_delete"),

]