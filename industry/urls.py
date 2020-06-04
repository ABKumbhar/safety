from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from industry.views import ApiAllView

router = DefaultRouter()

router.register(r'industry', views.IndustryViewSet)
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'qnai',views.QnaiViewSet)
router.register(r'qnae',views.QnaeViewSet)



urlpatterns = [
      path('', include(router.urls)),
      path('list',ApiAllView.as_view(),name="list"),

]
