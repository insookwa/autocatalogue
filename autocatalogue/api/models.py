from django.db import models



#brands model   
class Brand(models.Model):
    
    name = models.CharField(max_length=100,null=False,blank=False)
    logo = models.ImageField(upload_to='images/', default='image/None/No-img.jpg')
    created_at = models.DateTimeField(verbose_name='date created',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date updated',auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


#Models Model
class Model(models.Model):
    
    name = models.CharField(max_length=100,null=False,blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


#generations model 
class Generation(models.Model):
    
    name = models.CharField(max_length=100,null=False,blank=False)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = 'Generation '
        verbose_name_plural = 'Generations'


#cars Model
class Car (models.Model):
   name = models.CharField(max_length=100,null=False,blank=False)
   photo = models.ImageField(upload_to='images/', default='image/None/No-img.jpg')
   brand = models.ForeignKey(Brand,on_delete=models.SET_NULL, null=True, blank=True)
   model = models.ForeignKey(Model,on_delete=models.SET_NULL, null=True, blank=True)
   generation = models.ForeignKey(Generation,on_delete=models.SET_NULL, null=True, blank=True)
   description =description = models.TextField()

#Spare parts category model
class Category(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ImageField(upload_to='images/', default='image/None/No-img.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'  


#Spare parts model   
class Part(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    generation = models.ForeignKey(Generation,on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'part'
        verbose_name_plural = 'Parts'



