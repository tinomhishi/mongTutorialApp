from django.contrib import admin

from users.models import User

@admin.register(User)
class UniversalAdmin(admin.ModelAdmin):
    exclude = ('deleted_at','password', 'last_login')

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]