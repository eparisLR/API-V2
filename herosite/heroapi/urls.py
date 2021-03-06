# heroapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet) # The router works with a viewset to dynamically generate routes
router.register(r'creators', views.CreatorViewSet) # The router works with a viewset to dynamically generate routes
router.register(r'superpowers', views.SuperpowersViewSet) # The router works with a viewset to dynamically generate routes

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]