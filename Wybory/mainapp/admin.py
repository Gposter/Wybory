from django.contrib import admin

from .models import Kandydat
from .models import Wybory
from .models import osoba_gl
from .models import Lista
from .models import Lista_K
# Register your models here.
admin.site.register(Kandydat)
admin.site.register(Wybory)
admin.site.register(osoba_gl)
admin.site.register(Lista)
admin.site.register(Lista_K)
