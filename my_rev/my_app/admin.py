from django.contrib import admin
from my_app.models import AccessRecord,Topic,WebPage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
