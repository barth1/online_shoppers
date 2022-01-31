from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="categories"
        #this is to add plural to the word category


class Product(models.Model):
    mainimage = models.ImageField(upload_to='product')
    name = models.CharField(max_length=264)
    category =models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    details_text = models.TextField(max_length=1000, verbose_name='Description')
    price =models.FloatField()
    old_price =models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.name


    class Meta:
        ordering =['-created']
        # with we will be getting the product from our data base on a descending order