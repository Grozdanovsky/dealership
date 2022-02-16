from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('vehicles', views.VehicleViewSet)
router.register('type', views.TypeViewSet)
router.register('companies',views.CompanyViewSet)

urlpatterns = [
        path('user/',views.user_list),
        path('user/<int:pk>/',views.user_detail),

]

urlpatterns += router.urls 
