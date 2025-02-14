from django.urls import path
from .views import HeartRateCreateView, HeartRateListView

urlpatterns = [
    path('', HeartRateCreateView.as_view(), name='record-heart-rate'),
    path('patient/<int:patient_id>/', HeartRateListView.as_view(), name='patient-heart-rate'),
]
