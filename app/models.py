from django.db import models

# Create your models here.

class HeroItem(models.Model):
    image = models.ImageField(upload_to='hero_items')
    label = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'tb_Hero'

class TrendingProduct(models.Model):
    image1 = models.ImageField(upload_to='trending_products')
    episode = models.CharField(max_length=10)
    comments = models.IntegerField()
    views = models.IntegerField()
    status = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tb_TrendingProduct'

class TopView(models.Model):
    image = models.ImageField(upload_to='top_views')
    episode = models.CharField(max_length=10)
    views = models.IntegerField()
    name = models.CharField(max_length=100)
    filter_day = models.BooleanField(default=False)
    filter_week = models.BooleanField(default=False)
    filter_month = models.BooleanField(default=False)
    filter_year = models.BooleanField(default=False)

    class Meta:
        db_table = 'tb_TopView'

class NewComment(models.Model):
    image = models.ImageField(upload_to='new_comments')
    status = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    views = models.IntegerField() 

    class Meta:
        db_table = 'tb_NewComment'


class Anime(models.Model):
    name = models.CharField(max_length=100)

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to="videos/")
    thumbnail = models.ImageField(upload_to="thumbnails/")

    def __str__(self):
        return self.title

class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE,null=False, blank=False)
    number = models.CharField(max_length=10)

class Review(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    review_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    





