from django.contrib import admin
from UserManagement.models import UserAccount, UserProfile
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
	list_display = ('id','email', 'username', 'date_joined',
	                'last_login', 'is_superuser', 'is_active', 'is_staff')
	search_fields = ['email','username',]
	readonly_fields = ('date_joined','last_login')
	list_display_links = ('email','username',)

	filter_horizontal = ()
	list_filter = ('is_superuser','is_staff','is_active')
	fieldsets =(
			("User Details",{'fields':('username','email')}),
			("Account Details",{'fields':('date_joined','last_login')}),
			("Permission",{'fields':('is_active','is_staff','is_superuser')}),
            ('Group & Module Permissions', {
                'fields': ('groups', 'user_permissions', )
            }),
		)

	add_fieldsets=(
			
			("User Details",{'fields':('username','email','password1','password2')}),
			("Permission",{'fields':('is_active','is_staff','is_superuser')}),
		
		)


admin.site.register(UserAccount, AccountAdmin)
admin.site.register(UserProfile)

