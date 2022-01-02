from typing_extensions import TypeGuard
from django.db import models
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator
from UserManagement.models import UserAccount as User
import uuid

# Models with title and image (ecom m-1)
class Course(models.Model):
	title 			= models.CharField(max_length = 450, default='Default title !!!')
	image 			= models.ImageField(blank=True, null=True, default = 'CourseDefault.jpg',upload_to = 'Course/%Y/%m/',verbose_name="Main Image")
	image1 			= models.ImageField(blank=True, null=True, upload_to = 'Course/%Y/%m/',verbose_name="2nd Image")
	image2 			= models.ImageField(blank=True, null=True, upload_to = 'Course/%Y/%m/',verbose_name="3rd Image")
	image3 			= models.ImageField(blank=True, null=True, upload_to = 'Course/%Y/%m/',verbose_name="4th Image")
 
	price 			= models.DecimalField(decimal_places=2, max_digits=20, default=0,verbose_name="Course Price",validators=[MinValueValidator(0.0)])
	discount_price  = models.DecimalField(blank=True,null=True,decimal_places=2, max_digits=20, verbose_name="Discount Price",validators=[MinValueValidator(0.0)]) 
	slug 			= models.SlugField(blank=True,unique=True)
	description     = models.TextField(blank=True, null=True)
	additional_info = models.TextField(blank=True, null=True)
	category        = models.ManyToManyField('Category', verbose_name="category of course",blank=True)
	featured		= models.BooleanField(default=False, verbose_name="Featured Course")
	created			= models.DateTimeField(auto_now_add=True)
	modified 		= models.DateTimeField(auto_now=True)
	history			= HistoricalRecords()
	
	# label			= models.CharField(choices=LABEL_CHOICES, max_length=1)
 	# tag			= models.CharField(choices=LABEL_CHOICES, max_length=1)
	# autoTaged 	= models.CharField(choices=LABEL_CHOICES, max_length=1)
 	# created_by		= models.UUIDField(editable=False)
	# modified_by = models.UUIDField(editable=False)
 
 
	class Meta:
		ordering = ['-created']
		verbose_name_plural = 'Courses'
	
	def __str__(self):
		return self.title

	def __unicode__(self):
	    return self.title
 
	# def get_absolute_url(self):
	# 	return reverse("core:product",kwargs={'slug':self.slug})

	# def add_to_cart_url(self, path):
	# 	return reverse("core:add_to_cart",kwargs={'slug':self.slug,'redslug':path},)
    
	# def remove_from_cart_url(self,):
    # 		return reverse("core:remove_from_cart",kwargs={'slug':self.slug})

	# def cart_delete_url(self):
	# 	return reverse("core:delete_from_cart",kwargs={'slug':self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

