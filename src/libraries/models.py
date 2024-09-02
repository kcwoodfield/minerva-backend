from django.db import models


# LibraryEntry model for a Book
class LibraryEntry(models.Model):
    title = models.CharField(max_length=265)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    rating = models.IntegerField()
    review = models.TextField()
    isbn = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
