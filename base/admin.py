from django.contrib import admin
from .models import Transaction
from .models import Register


admin.site.register(Transaction)
admin.site.register(Register)


