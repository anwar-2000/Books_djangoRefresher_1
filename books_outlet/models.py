from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    isBestSelling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def save(self ,*args, **kwargs):
        #calling this method will trigger cthis line then the actuall save method
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get__absolute__url(self):
        return reverse('book-detail', args=[self.id])

    def __str__(self) :
        return f"{self.title} ({self.rating})"

