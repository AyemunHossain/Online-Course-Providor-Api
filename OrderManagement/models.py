from django.db import models
from django.utils import tree
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator
from UserManagement.models import UserAccount as User
import uuid
from CourseManagement.models import Course
# Models with title and image (ecom m-1)



class OrderCourse(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    item        = models.ForeignKey(Course, on_delete=models.CASCADE)
    ordered     = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} : {self.item} : enrolled by {self.user}"

    # def get_total_course_price(self):
    #     if (self.course.discount_price != None) and (self.course.discount_price > 0):
    #         return (self.quantity*self.course.discount_price)
    #     else:
    #         return (self.quantity*self.course.price)

    # def get_saved_amount(self):
    #      if (self.course.discount_price != None) and (self.course.discount_price > 0):
    #         return (self.quantity*self.course.price)-self.get_total_course_price()
    #      else:
    #          return None

    # def get_course_total_quantity(self):
    #         return (self.quantity)


class Order(models.Model):
    """[This models is managing the card and checkout process]
        [It takes the use,items[which is the manytomany field of OrderItem class]]
    """
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    items                   = models.ManyToManyField(OrderCourse)
    refrence_code           = models.CharField(max_length=50, unique=True, null=True, blank=True,)
    start_date              = models.DateTimeField(auto_now_add=True)
    ordered_completion_date = models.DateTimeField(null=True, blank=True,)
    ordered                 = models.BooleanField(default=False)
    billing_address         = models.ForeignKey('BillingAddress', null=True, blank=True,
                                        on_delete=models.SET_NULL)
    # payment         		= models.ForeignKey('Payment', null=True, blank=True,
    #                 		        on_delete=models.SET_NULL)
    coupon                  = models.ForeignKey('Coupon', null=True, blank=True,
                               on_delete=models.SET_NULL)

    payment_status          = models.BooleanField(default=False)
    # delivering              = models.BooleanField(default=False)
    # recieved                = models.BooleanField(default=False)
    # refund_request          = models.BooleanField(default=False)
    # refund_granted          = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.refrence_code}: {self.id} : of {self.user.username}"

    # def total_quantity (self):
    #     total = 0
    #     for q in self.items.all():
    #         total += int(q.get_item_total_quantity())
    #     return total

    # def get_total_bill(self):
    #     total = 0
    #     for order_item in self.items.all():
    #         total += order_item.get_total_item_price()
    #     if self.coupon:
    #         total -=int(self.coupon.amount)
    #     return total

    # def get_total_saving(self):
    #     total = 0
    #     for order_item in self.items.all():
    #         if order_item.get_saved_amount():
    #         	total += order_item.get_saved_amount()
    #     if total ==0:
    #         return None
    #     return total


class BillingAddress(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    address             = models.CharField(max_length=300)
    apartment_address   = models.CharField(max_length=200)
    #country 				= CountryField(multiple=False)
    zipcode             = models.CharField(max_length=5)
    save_info           = models.BooleanField(default=False)
    #payment_method 			= models.CharField(choices=PAYMENT_CHOICES, max_length=2)

    def __str__(self):
        return f"{self.user.username}'s Billing Address"


class Coupon(models.Model):
    code        = models.CharField(max_length=100)
    amount      = models.FloatField()

    class Meta:
        ordering = ['amount']

    def __str__(self):
        return self.code



class Payment(models.Model):
    order_ref = models.TextField(max_length=100, verbose_name="Order Reference", blank=True ,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True )
    stripe_charge_id = models.CharField(max_length=100,null=True, blank=True )
    amount = models.FloatField(default=0.0)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -  {self.stripe_charge_id}"
