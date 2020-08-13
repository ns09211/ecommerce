from django.db import models
# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    subcategory=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to="shop/images")
    pub_date=models.DateField()
    desc=models.CharField(max_length=300)
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,default="")
    phone=models.CharField(max_length=12,default="")
    desc=models.CharField(max_length=300,default="")
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000,default="")
    name = models.CharField(max_length=30,default="")
    email = models.EmailField(max_length=50,default="")
    address = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=50,default="")
    state= models.CharField(max_length=50,default="")
    zip_code = models.CharField(max_length=6,default="")
    phone = models.CharField(max_length=12,default="")
    amount=models.IntegerField()

class orderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=5000,default='')
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"........"

