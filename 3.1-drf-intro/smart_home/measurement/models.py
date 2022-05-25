from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)



class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
