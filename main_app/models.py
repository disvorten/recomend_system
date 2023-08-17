from django.db import models
from django.contrib.auth.models import AbstractUser


class Books(models.Model):
    book_id = models.IntegerField()
    books_count = models.IntegerField( blank=True, null=True)
    isbn = models.IntegerField(blank=True, null=True)
    authors = models.CharField(max_length=100, blank=True, null=True)
    original_publication_year = models.IntegerField( blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    language_code = models.CharField(max_length=10, blank=True, null=True)
    average_rating = models.FloatField(max_length=5, blank=True, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    small_image_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '//'.join(
            [f'title name = {self.title}', f'author = {self.authors}', f'aver_rating = {str(self.average_rating)}'])

    def get_absolute_url(self):
        return f'./{self.id}'

    class Meta:
        ordering = ['id']


class User(AbstractUser):
    first_name = models.CharField(max_length=50, default='', blank=True, null=True)
    last_name = models.CharField(max_length=50, default='', blank=True, null=True)
    read_books = models.CharField(max_length=1000, default='', blank=True, null=True)
    recomm_books = models.CharField(max_length=100, default='', blank=True, null=True)
    checked_items = models.CharField(max_length=100, default='', blank=True, null=True)
    model_existence = models.BooleanField(default=False)

    def __str__(self):
        return ''.join([self.first_name, self.last_name])

    # def get_absolute_url(self):
    #     return f'./{self.id}'


class Ratings(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)
