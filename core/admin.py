from django.contrib import admin
from .models import *
# Register your models here.

class AnaliseAdmin(admin.ModelAdmin):
    pass
class ClasseAdmin(admin.ModelAdmin):
    pass
class DataAdmin(admin.ModelAdmin):
    pass
class TableAdmin(admin.ModelAdmin):
    pass

admin.site.register(Analise, AnaliseAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Table, TableAdmin)
