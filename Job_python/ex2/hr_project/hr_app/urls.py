from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home),
    path('addemp',views.addemp),
    path('manage',views.manage),
    path('list',views.list),
    path('login',views.custom_login),
    path('logout' ,views.logout_view)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)