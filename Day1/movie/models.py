from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.IntegerField()
    username=models.CharField(max_length=100)

class Movie(models.Model):
    movieId=models.IntegerField(unique=True)
    title=models.CharField(max_length=200)
    genres=models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [ models.Index(fields=['title']) ]
    
class Link(models.Model):
    movieId = models.OneToOneField(Movie, on_delete=models.CASCADE)
    imdbId = models.IntegerField(blank=True, null=True)
    tmdbId = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return f"link of {self.movieId}"
    
class Rating(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    timestamp = models.IntegerField()

    class Meta:
        unique_together = ('userId', 'movieId')

class Tag(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
    timestamp = models.IntegerField()

    class Meta:
        unique_together = ('userId', 'movieId')
