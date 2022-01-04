from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.base import Model


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name=None, last_name=None, password=None):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")

        user_obj = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(verbose_name='email', unique=True, max_length=60)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_lebel):
        return True


class UserProfile(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="account")
    avatar = models.ImageField(blank=True, null=True, default='UserAvatar/df_Avatar.jpg',upload_to='UserAvatar/%Y/%m/%d/', verbose_name="Profile Avatar")
    slug = models.SlugField(blank=True, unique=True)
    #gender = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(validators=[MinValueValidator(15.0),MaxValueValidator(100.0)])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.id}"+" -Profile"
