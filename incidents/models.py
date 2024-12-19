from django.db import models
import random
from django.utils import timezone
from users.models import User


# Incident Model
class Incident(models.Model):
    INCIDENT_PRIORITIES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    INCIDENT_STATUS = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    ENTERPRISE_OR_GOVERNMENT = [
        ('Enterprise', 'Enterprise'),
        ('Government', 'Government'),
    ]

    # Fields
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_id = models.CharField(max_length=20, unique=True)
    details = models.TextField()
    priority = models.CharField(max_length=10, choices=INCIDENT_PRIORITIES, default='Medium')
    status = models.CharField(max_length=20, choices=INCIDENT_STATUS, default='Open')
    created_at = models.DateTimeField(default=timezone.now)
    enterprise_or_government = models.CharField(max_length=20, choices=ENTERPRISE_OR_GOVERNMENT)

    # Custom methods for Incident ID and Uniqueness
    def generate_incident_id(self):
        random_number = random.randint(10000, 99999)
        return f"RMG{random_number}{timezone.now().year}"

    def check_unique_incident_id(self):
        # Check if incident ID already exists in the database
        return not Incident.objects.filter(incident_id=self.incident_id).exists()

    def save(self, *args, **kwargs):
        if not self.incident_id:
            self.incident_id = self.generate_incident_id()
        # Ensure uniqueness of incident ID
        while not self.check_unique_incident_id():
            self.incident_id = self.generate_incident_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.incident_id

    # Auto-fill user details if they exist
    def auto_fill_reporter_details(self):
        # Assuming that User model has fields like name, email, etc.
        if self.reporter:
            self.reporter_name = self.reporter.name  # or other fields
            self.reporter_email = self.reporter.email  # or other fields

    # Ensure that incidents with 'Closed' status cannot be edited
    def is_editable(self):
        return self.status != 'Closed'

    # Custom manager to filter incidents by the logged-in user
    @classmethod
    def get_user_incidents(cls, user):
        return cls.objects.filter(reporter=user)

    # Search method for Incident ID
    @classmethod
    def search_by_incident_id(cls, incident_id):
        return cls.objects.filter(incident_id__icontains=incident_id)
