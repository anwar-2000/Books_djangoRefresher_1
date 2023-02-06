from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name= models.CharField(max_length=20)
    code = models.CharField(max_length=2)

class Adresse(models.Model):
    street = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.street} , {self.city} , {self.postal_code}"


class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    addresse = models.OneToOneField(Adresse , on_delete=models.CASCADE,null=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    isBestSelling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)
    published_books = models.ManyToManyField(Country)

    def save(self ,*args, **kwargs):
        #calling this method will trigger cthis line then the actuall save method
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get__absolute__url(self):
        return reverse('book-detail', args=[self.id])

    def __str__(self) :
        return f"{self.title} ({self.rating})"

