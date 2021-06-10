from django.db import models

# Create your models here.
class Blog(models.Model):
    """This class will hold the name of the blog."""
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    #A method that returns the name of our blog as a string.
    def __str__(self):
        return self.name

class Author(models.Model):
    """Class that holds the model for Author"""
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    """This will hold the entire format of the blog entry."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline