from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin,SummernoteInlineModelAdmin
from django_summernote.utils import get_attachment_model 

# Register your models here.

class GateAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    pass


admin.site.register(Industry)
admin.site.register(Equipment)
admin.site.register(Qnai)
admin.site.register(Qnae)
admin.site.register(Gate, GateAdmin)