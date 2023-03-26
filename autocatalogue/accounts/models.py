from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)


#User Creation Models 
class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError('Users should have a username ')
        if email is None:
            raise TypeError('Users should have an Email')
        
        user=self.model(username=username, email = self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError('Password should not be none')
        
        user=self.create_user(username,email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique=True,db_index=True)
    email = models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        return ''
#brands model   
class Brand(models.Model):
    
    name = models.CharField(max_length=100,null=False,blank=False)
    logo = models.ImageField(null=False, blank=False)
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
   logo = models.ImageField(null=False, blank=False)
   brand = models.ForeignKey(Brand,on_delete=models.SET_NULL, null=True, blank=True)
   model = models.ForeignKey(Model,on_delete=models.SET_NULL, null=True, blank=True)
   Generation = models.ForeignKey(Generation,on_delete=models.SET_NULL, null=True, blank=True)
   description =description = models.TextField()

class Category(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)

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

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'part'
        verbose_name_plural = 'Parts'