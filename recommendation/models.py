from django.db import models
from customer.models import Customer
# Create your models here.
class RecommendedMovies(models.Model):
    user = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)
    recommendations = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommended_movies'

    def __str__(self):
        return "Recommender for user: " +self.user.name