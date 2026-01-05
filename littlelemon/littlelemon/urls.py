from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views


from restaurant.views import UserViewSet, BookingViewSet

# router for users (global)
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# router for booking (coursera)
booking_router = routers.DefaultRouter()
booking_router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # existing restaurant app routes (index + menu)
    path('restaurant/', include('restaurant.urls')),

    # DRF user API
    path('', include(router.urls)),

    # booking API exactly where Coursera wants it
    path('restaurant/booking/', include(booking_router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]