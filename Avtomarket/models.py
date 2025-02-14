from django.db import models

class Avtosalon(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Car(models.Model):
    model = models.CharField(max_length=255)
    ot_kuchi = models.IntegerField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    yili = models.IntegerField()
    avtosalon = models.ForeignKey(Avtosalon, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return f"{self.model} ({self.yili})"
