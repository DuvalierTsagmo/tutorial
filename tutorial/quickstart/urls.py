from rest_framework import routers
from quickstart.views import BandSerializer, ListingSerializer, VoitureSerializer

router = routers.DefaultRouter()
router.register('bands', BandSerializer) #Enregistre la route
router.register('listing', ListingSerializer)
router.register('voiture', VoitureSerializer)

#Par la suite importer nos urls dans le url root se trouvant dans le meme dossier que settings.py