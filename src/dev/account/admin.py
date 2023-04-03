from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('pk', 'email', 'is_email_confirmed', 'first_name', 'last_name', 'is_admin', 'is_active', 'last_login')
    list_filter = ('is_admin',)
    list_editable = ('is_email_confirmed',)
    fieldsets = (
        (None, {'fields': ('email', 'email_id', 'first_name', 'last_name', 'password')}),
        ('Разрешения', {'fields': ('is_admin', 'is_active')}),
        ('Даты', {'fields': ('date_joined', 'last_login')}),
    )
    readonly_fields = ('date_joined', 'email_id')
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
