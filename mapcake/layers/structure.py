#!/usr/bin/python2.4
# -*- coding: utf-8 -*

"""TODO faire tests unitaires"""

"""Les couches recuperees depuis les services"""

caracteresReservesJavaScript = [" ", "-", ".", '"', "'", "@",
                                ":", "/", "+", "*", "%", "=", "~", "!",
                                "?", "<", ">", "(", ")",
                                "[", "]", "{", "}", "#", "&", "|", "`", "^",
                                "¨", "€"]


class LayerServices:
    def __init__(self, wms, nom):
        self.wms = wms
        self.nom = nom
        self.id = nom
        for currentCaractere in caracteresReservesJavaScript:
            self.id = self.id.replace(currentCaractere, '__')
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
