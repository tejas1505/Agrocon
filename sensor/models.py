from django.db import models



class records(models.Model):
    plant_name2 = models.CharField(max_length=20)
    sensor_value2 = models.IntegerField()
    value_date2 = models.DateField(auto_now_add=True)
    value_time2 = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.plant_name2

# Create your models here.
class sensor_register(models.Model):
    register_no = models.AutoField(primary_key=True)
    device_no = models.IntegerField()
    sen_longitude = models.DecimalField(max_digits=7,decimal_places=6, default=1.0)
    sen_latitude = models.DecimalField(max_digits=7,decimal_places=6, default=1.0)
    date = models.DateField(auto_now=True)
    time_zone = models.TimeField(auto_now=True)
    sen_type = models.CharField(max_length=20)
    plant_name = models.CharField(max_length=20)
    measurement = models.IntegerField()
    plot_id = models.IntegerField()
    crop = models.CharField(max_length=50,default=False)
    sensor_value = models.IntegerField(default=0,blank=True)
    value_date = models.DateField(auto_now=True,blank=True)
    value_time = models.TimeField(auto_now=True,blank=True)
    # active = models.CharField(max_length=5, default="False", blank=True)
    # inactive = models.CharField(max_length=5, default="False", blank=True)

    def __str__(self):
        return self.plant_name