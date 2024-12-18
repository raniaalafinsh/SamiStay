from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile
from .models import Apartment


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'is_staff', 'get_role')
    list_select_related = ('profile',)

    def get_role(self, instance):
        return instance.profile.role if hasattr(instance, 'profile') else None
    get_role.short_description = 'Role'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('location', 'rooms', 'price', 'size', 'university', 'new_construction')