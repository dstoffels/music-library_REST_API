from django.db import models

# Create your models here.

class Song(models.Model):
  title = models.CharField(max_length = 50)
  artist = models.CharField(max_length=50)
  album = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  release_date = models.DateField()
  likes = models.IntegerField(default=0)
  image = models.ImageField(upload_to='images', null=True)

  def like(self):
    self.likes += 1
    self.save()

