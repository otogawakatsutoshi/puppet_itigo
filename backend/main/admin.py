from django.contrib import admin

# Register your models here.
from .models import Book,HtmlTag

admin.site.register(Book)

admin.site.register(HtmlTag)