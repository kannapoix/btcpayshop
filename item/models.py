from django.db import models
from django.utils import timezone
from shop.models import Shop

def shop_directory_path(instance, filename):
    return 'shop_{0}/{1}'.format(instance.shop.id, filename)

class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    btcpay_item_name = models.CharField(max_length=200)
    price = models.IntegerField()
    image_path = models.FileField(upload_to=shop_directory_path, null=True)
    is_active = models.BooleanField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
