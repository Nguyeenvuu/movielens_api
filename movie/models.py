from django.db import models

# Create your models here.

class Movies(models.Model):
    belongs_to_collection   = models.TextField(blank=True, null=True)
    budget                  = models.IntegerField(blank=True, null=True)
    genres                  = models.TextField(blank=True, null=True)
    homepage                = models.TextField(blank=True, null=True)
    movie_id                = models.IntegerField(primary_key=True) # Khóa chính
    original_language       = models.TextField(blank=True, null=True)
    title                   = models.TextField(blank=True, null=True)
    overview                = models.TextField(blank=True, null=True)
    popularity              = models.FloatField(blank=True, null=True)
    poster_path             = models.TextField(blank=True, null=True)
    production_companies    = models.TextField(blank=True, null=True)
    release_date            = models.TextField(blank=True, null=True)
    revenue                 = models.BigIntegerField(blank=True, null=True)
    runtime                 = models.IntegerField(blank=True, null=True)
    tagline                 = models.TextField(blank=True, null=True)
    vote_average            = models.FloatField(blank=True, null=True)
    vote_count              = models.IntegerField(blank=True, null=True)
    actor                   = models.TextField(blank=True, null=True)
    director                = models.TextField(blank=True, null=True)
    backdrop_path           = models.TextField(blank=True, null=True)
    # table movies cần được tạo trước khi makemigrations và migrate
    class Meta:
        managed     = False
        db_table    = 'movies' # table trong database
    
    def __str__(self):
        return self.title

