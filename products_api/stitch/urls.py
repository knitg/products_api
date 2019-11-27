from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'upload', views.ImageViewSet)
router.register(r'stitch', views.StitchViewSet)
router.register(r'stitch-types', views.StitchTypeViewSet)
router.register(r'stitch-type-design', views.StitchTypeDesignViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'productbyuser/(?P<user_id>\d+)', views.ProductByUserViewSet)
router.register(r'stitchtype/(?P<stitch_id>\d+)', views.StitchTypeByStitchViewSet)

urlpatterns = [ 
    path('', include(router.urls))
]
