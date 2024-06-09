from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ISDTeamProject import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('Users.urls')),
    path('products/', include('products.urls')),
    path('delivery/', include('deliveries.urls')),
    path('shipment/', include('shipment.urls')),
    path('supplier/', include('suppliers.urls')),
    path('orders/', include('orders.urls')),
    path('homepage/',views.homepage, name='homepage'),
    #path('accounts/', include('django.contrib.auth.urls')),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
