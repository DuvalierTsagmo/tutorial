from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'band', views.BandViewSet)
router.register(r'listing', views.ListingViewSet)
router.register(r'voiture', views.VoitureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('listings/', views.list),
    path('bands/', views.ban),
    path('voitures/', views.voit),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]