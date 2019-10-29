from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'types', views.StitchTypeViewSet)
router.register(r'designs', views.StitchTypeDesignViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]
