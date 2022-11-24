from rest_framework import routers
from language.views import BandSerializer, ListingSerializer

router = routers.DefaultRouter()
router.register('bands', BandSerializer) #Enregistre la route
router.register('listing', ListingSerializer)

#Par la suite importer nos urls dans le url root se trouvant dans le meme dossier que settings.py