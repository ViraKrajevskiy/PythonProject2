from django.db import models

class CarModel(models.Model):
    title = models.CharField(max_length=255)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Car(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    context = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return f"{self.title} ({self.year})"
