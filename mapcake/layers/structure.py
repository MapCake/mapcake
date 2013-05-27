"""TODO faire tests unitaires"""

"""Les couches recuperees depuis les services"""


class LayerServices:
    def __init__(self, wms, nom):
        self.wms = wms
        self.nom = nom
        self.id = nom.replace(".", "__")
        self.boundingBox = wms[nom].boundingBoxWGS84
        self.lstStyles = []
        for currentStyleName in wms[nom].styles.keys():
            self.lstStyles.append(
                LayerStyle(
                    currentStyleName,
                    wms[nom].styles[currentStyleName]))

"""Le style d'une couche"""


class LayerStyle:
    def __init__(self, nom, currentElemStyle):
        self.nom = nom
        self.titre = currentElemStyle['title']
        self.url = currentElemStyle['legend']
