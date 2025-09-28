from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    list_display=('id','email','name','tc','is_admin')
    list_filter=('is_admin',)
    fieldsets=(
        ('User_Credentials',{'fields':('email','password')}),
        ('Personal_info',{'fields':('name','tc')}),
        ('Permission',{'fields':('is_admin',)}),
    )
    
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','name','password1','password2')
        })
    )
    search_fields=('email',)
    ordering=('email','id')
    filter_horizontal=()
    
admin.site.register(User,UserModelAdmin)