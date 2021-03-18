from django.db import models
from movie.models import Movies
from customer.models import Customer
# Create your models here.
class Ratings(models.Model):
    user = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)
    movie = models.ForeignKey(Movies, models.DO_NOTHING, default=8)
    rating = models.FloatField(blank=True, null=True, default=5)
    time_rating = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ratings'
        unique_together = (('user', 'movie'),)

    def __str__(self):
        return str(self.user.name) + ":" + str(self.movie.title)