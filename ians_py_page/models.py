from django.db import models

# Create your models here.
class Topic(models.Model):
    """A class that represents the topic of a blog post."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Body(models.Model):
    """This will hold the body of the blog post."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'bodies'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text