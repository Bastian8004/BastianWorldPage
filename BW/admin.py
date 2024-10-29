import os
import uuid
import zipfile
import mysite.settings
from datetime import datetime
from zipfile import ZipFile

from django.contrib import admin
from django.core.files.base import ContentFile

from PIL import Image

from BW.models import Services, Qualifications, Contakt, Start, BlogS, BlogBW, PostS, PostBW, CheckoutSessionRecord
from BW.forms import ServicesForm


admin.site.register(Start)
admin.site.register(Services)
admin.site.register(Qualifications)
admin.site.register(Contakt)
admin.site.register(CheckoutSessionRecord)


class PostBWInline(admin.TabularInline):
    model = PostBW

@admin.register(BlogBW)
class BlogBWAdmin(admin.ModelAdmin):
    inlines = [
        PostBWInline,
    ]


class PostSInline(admin.TabularInline):
    model = PostS

@admin.register(BlogS)
class BlogSAdmin(admin.ModelAdmin):
    inlines = [
        PostSInline,
    ]