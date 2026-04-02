from django.contrib import admin
from .models import LoanApplication


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    # This makes the list view look like a spreadsheet
    list_display = ('full_name', 'loan_amount', 'status', 'created_at')

    # This adds a sidebar to filter by status or date
    list_filter = ('status', 'created_at')

    # This adds a search bar for names and emails
    search_fields = ('full_name', 'email')

    # This allows you to change the status directly from the list!
    list_editable = ('status',)