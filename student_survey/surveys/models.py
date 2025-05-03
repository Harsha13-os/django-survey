from django.db import models

# Create your models here.
class Survey(models.Model):
    LIKE_CHOICES = [
        ('students', 'Students'),
        ('location', 'Location'),
        ('campus', 'Campus'),
        ('atmosphere', 'Atmosphere'),
        ('dorms', 'Dorm Rooms'),
        ('sports', 'Sports'),
    ]

    INTEREST_CHOICES = [
        ('friends', 'Friends'),
        ('television', 'Television'),
        ('internet', 'Internet'),
        ('other', 'Other'),
    ]

    RECOMMEND_CHOICES = [
        ('very_likely', 'Very Likely'),
        ('likely', 'Likely'),
        ('unlikely', 'Unlikely'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_survey = models.DateField()
    liked_most = models.CharField(max_length=50, choices=LIKE_CHOICES)
    interested_via = models.CharField(max_length=50, choices=INTEREST_CHOICES)
    recommend = models.CharField(max_length=20, choices=RECOMMEND_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"