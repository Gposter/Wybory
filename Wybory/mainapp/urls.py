from django.conf.urls import url
from . import views
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('login',views.login ,name='login'),
    path('zaloguj<id_w>',views.zaloguj,name='zaloguj'),
    path('index',views.menup,name='menup'),
    path('glos',views.glos,{'b':'b'},name='glos'),
    path('glowna',views.glowna,name='glowna'),
    path('wybory_K',views.glowna2,name='glowna2'),
    path('Kandydaci<id_w>',views.kand,name='kand'),
    path('Zapytanie',views.zapytanie,name='zapytanie'),
    path('wynik',views.wynik,name='wynik'),
    path('pdf<id_w>',views.get,name='pdf'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
