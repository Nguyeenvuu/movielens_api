from django.db import models
from movie.models import Movies
from customer.models import Customer
# Create your models here.
class Comment(models.Model):
    id          = models.AutoField(primary_key=True)
    user        = models.ForeignKey(Customer, models.DO_NOTHING)
    movie       = models.ForeignKey(Movies, models.DO_NOTHING)
    content     = models.TextField(blank=True, null=True)
    timestamp   = models.DateField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'comment'

    def __str__(self):
        return str(self.user.name) + ":" + str(self.movie.title)