from django.db import models

# Create your models here.
class AvlTest(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default = 0)
    items = models.ManyToManyField('AvlTest', related_name='order', blank=True)
    # doctor_consulation = models.ManyToManyField('Doctor', related_name='doctor', blank=True)

    name = models.CharField(max_length = 50, blank=True)
    email = models.CharField(max_length = 50, blank=True)
    phone = models.CharField(max_length = 10, blank=True)
    street = models.CharField(max_length = 50, blank=True)
    pin_code = models.IntegerField(blank = True, null=True)
    date = models.DateTimeField(blank = True, null=True)

    is_paid = models.BooleanField(default = False)
    # is_doctor_consulation = models.BooleanField(default = False)
    # is_report_ready =  models.BooleanField(default = False)
    
    def __str__(self) :
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'

class Doctor(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    appt_charges = models.DecimalField(max_digits=7, decimal_places=2)
    
    name = models.CharField(max_length = 50, blank=True)
    email = models.CharField(max_length = 50, blank=True)
    street = models.CharField(max_length = 50, blank=True)
    pin_code = models.IntegerField(blank = True, null=True)

    def __str__(self) :
        return f'Doctor Consultaion: {self.created_on.strftime("%b %d %I: %M %p")}'
