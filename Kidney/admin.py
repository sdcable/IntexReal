from django.contrib import admin
from .models import client, single_serving_food_item, dailydiary, journalentry, serum_entry

# Register your models here.
admin.site.register(client)
admin.site.register(single_serving_food_item)
admin.site.register(dailydiary)
admin.site.register(journalentry)
admin.site.register(serum_entry)
