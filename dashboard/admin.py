# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from dashboard.models import Config, Note

admin.site.register(Config)
admin.site.register(Note)