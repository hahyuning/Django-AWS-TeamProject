from django.db import models

# Create your models here.
class Goo(models.Model):
    gu = models.CharField(max_length=100)

class Traffic(models.Model):
        register_car = models.PositiveIntegerField()
        parking_lot = models.PositiveIntegerField()
        bike = models.PositiveIntegerField()
        bus = models.PositiveIntegerField()
        trail = models.PositiveIntegerField()
        bus_trail = models.PositiveIntegerField()
        mycar = models.PositiveIntegerField()
        gu = models.ForeignKey(Goo, on_delete=models.CASCADE)

class Education(models.Model):
    garden = models.FloatField()
    element = models.FloatField()
    middle = models.FloatField()
    high = models.FloatField()
    garden_num= models.FloatField()
    element_num = models.FloatField()
    middle_num = models.FloatField()
    high_num = models.FloatField()
    garden_gyo = models.FloatField()
    element_gyo = models.FloatField()
    middle_gyo = models.FloatField()
    high_gyo = models.FloatField()
    gu = models.ForeignKey(Goo, on_delete=models.CASCADE)

class SeoulData(models.Model):
    safety = models.FloatField()
    medical = models.FloatField()
    medical_room = models.FloatField()
    environment = models.FloatField()
    traffic = models.FloatField()
    education = models.FloatField()
    gu = models.ForeignKey(Goo, on_delete=models.CASCADE)

class EnvironmentData(models.Model):
    park = models.FloatField()
    garbage = models.FloatField()
    dust = models.FloatField()
    green = models.FloatField()
    gu = models.ForeignKey(Goo, on_delete=models.CASCADE)

class Medical_CrimeData2(models.Model):
    hospital = models.FloatField()
    pharmacy = models.FloatField()
    sickbed = models.FloatField()
    crime_occ = models.FloatField()
    crime_arr = models.FloatField()
    gu = models.ForeignKey(Goo, on_delete=models.CASCADE)