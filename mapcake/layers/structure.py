#!/usr/bin/python2.4
# -*- coding: utf-8 -*
from psycopg2.extensions import AsIs

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


### a layer for an SQL table
### base sur
#http://gis.stackexchange.com/questions/52818/how-to-connect-openlayers-to-postgis-data
class LayerTable:
    def __init__(self, cursor, name):
        self.name = str(name)
        self.id = self.name
        print 'name'
        print name
        for currentCaractere in caracteresReservesJavaScript:
            self.id = self.id.replace(currentCaractere, '__')
        self.geoJSon = None
        # get name of the geometry column
        cursor.execute(
            "SELECT f_geometry_column FROM geometry_columns WHERE f_table_name  = \'%s\'",
            (AsIs(self.name),))
        if (cursor.rowcount > 0):
            nameColumn = cursor.fetchone()
            nameColumn = str(nameColumn[0])
            print "Name column"
            print nameColumn
            cursor.execute(
                "SELECT ST_AsGeoJSON(%s) FROM %s",
                (AsIs(nameColumn), AsIs(self.name)))
            self.geoJSon = cursor.fetchone()
