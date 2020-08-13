from django.db import models

# Create your models here.
class blogPost(models.Model):
    blog_id=models.AutoField
    title=models.CharField(max_length=50,default="")
    head0=models.CharField(max_length=500,default="")
    chead0 = models.CharField(max_length=500,default="")
    head1 = models.CharField(max_length=500,default="")
    chead1 = models.CharField(max_length=500,default="")
    head2 = models.CharField(max_length=500,default="")
    chead2 = models.CharField(max_length=500,default="")
    thumbmail=models.ImageField(upload_to="blog/images",default="")
    pub_date=models.DateField()

    def __str__(self):
        return self.title
