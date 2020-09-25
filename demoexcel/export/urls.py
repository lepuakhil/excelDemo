from django.urls import path
from .views import export_users_xls, index


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('export.urls')),
    path('home/', index),
    path('export/excel', export_users_xls, name='export_excel'),
]