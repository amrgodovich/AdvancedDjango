from django.contrib import admin
from .models import User,Tag,Rating,Link,Movie
# Register your models here.

# admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(Link)
