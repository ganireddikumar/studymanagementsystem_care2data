from django.db import models

class Study(models.Model):
    study_name = models.CharField(max_length=100)
    study_description = models.TextField()
    STUDY_PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]
    study_phase = models.CharField(max_length=10, choices=STUDY_PHASE_CHOICES)
    sponsor_name = models.CharField(max_length=100)
    class Meta:
        app_label = 'studies'

    def __str__(self):
        return self.study_name

