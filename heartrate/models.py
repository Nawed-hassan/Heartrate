from django.db import models
from patients.models import Patient

class HeartRate(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="heart_rates")
    bpm = models.PositiveIntegerField()  # Beats per minute
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.bpm} BPM"
