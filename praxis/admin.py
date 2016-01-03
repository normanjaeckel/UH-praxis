from django.contrib.admin import site
from django.contrib.auth.models import Group

from .models import Section


site.register(Section)
site.unregister(Group)
