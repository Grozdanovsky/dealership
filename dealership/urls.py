from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('vehicles', views.VehicleViewSet)
router.register('type', views.TypeViewSet)
router.register('companies',views.CompanyViewSet)


urlpatterns = [
        path('user/',views.UserList.as_view()),
        path('user/<int:pk>/',views.UserDetail.as_view()),
        path('user-service/',views.UserServiceVehicleList.as_view()),
        path('user-service/<int:pk>/',views.UserServiceVehicleDetail.as_view()),
        

]

urlpatterns += router.urls 
