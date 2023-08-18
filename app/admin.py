from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(HeroItem)
admin.site.register(TrendingProduct)
admin.site.register(TopView)
admin.site.register(NewComment)
admin.site.register(Anime)
admin.site.register(Video)
admin.site.register(Episode)
admin.site.register(Review)

