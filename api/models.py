from django.db import models

class Client(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    def __str__(self):
        return f'Client ID: {self.id}'


class Driver(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    def __str__(self):
        return f'Driver ID: {self.id}'


class Order(models.Model):
    STATUS_CHOICES = (
            ('created', 'Created'),
            ('cancelled', 'Cancelled'),
            ('accepted', 'Accepted'),
            ('finished', 'Finished'),
    )
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    driver=models.ForeignKey(Driver, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Order ID: {self.id}'