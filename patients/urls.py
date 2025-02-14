from django.urls import path
from .views import PatientCreateView, PatientDetailView

urlpatterns = [
    path('', PatientCreateView.as_view(), name='add-patient'),
    path('<int:pk>/', PatientDetailView.as_view(), name='get-patient'),
]
