from django.contrib import admin
from info_form.models import User_input
# Register your models here.




class InputsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'services_desired')


admin.site.register(User_input, InputsAdmin)