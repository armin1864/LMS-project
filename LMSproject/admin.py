from django.contrib import admin
from authors.models import Authors
from books.models import Books
from borrows.models import BorrowTransactions
from reservations.models import Reservations
from django.contrib.auth.admin import UserAdmin
from user_profile.forms import CustomUserCreationForm, CustomUserChangeForm
from user_profile.models import User

admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(BorrowTransactions)
admin.site.register(Reservations)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'registration_date',
                    'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'registration_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',
                       'phone_number', 'registration_date', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
