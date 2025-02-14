from rest_framework import generics
from .models import HeartRate
from .serializers import HeartRateSerializer

class HeartRateCreateView(generics.CreateAPIView):
    queryset = HeartRate.objects.all()
    serializer_class = HeartRateSerializer

class HeartRateListView(generics.ListAPIView):
    serializer_class = HeartRateSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return HeartRate.objects.filter(patient_id=patient_id)
