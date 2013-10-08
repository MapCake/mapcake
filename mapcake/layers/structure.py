#!/usr/bin/python2.4
# -*- coding: utf-8 -*
import time
from psycopg2.extensions import AsIs
from django.contrib.gis.gdal import DataSource

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
        self.name = nom
        self.id = nom.decode('utf-8')
        self.id = self.id.encode("ascii", "ignore")
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
        self.name = nom
        self.titre = currentElemStyle['title']
        self.url = currentElemStyle['legend']


### a layer for an SQL table
### base sur
#http://gis.stackexchange.com/questions/52818/how-to-connect-openlayers-to-postgis-data
class LayerTable:
    def __init__(self, cursor, name):
        self.name = str(name)
        self.id = self.name
        for currentCaractere in caracteresReservesJavaScript:
            self.id = self.id.replace(currentCaractere, '__')
        self.geoJSonTab = None
        # get name of the geometry column
        cursor.execute(
            "SELECT f_geometry_column FROM geometry_columns WHERE f_table_name  = \'%s\'",
            (AsIs(self.name),))
        if (cursor.rowcount > 0):
            nameColumn = cursor.fetchone()
            nameColumn = str(nameColumn[0])
            tpsdebJSon = time.clock()
            cursor.execute(
                "SELECT ST_AsGeoJSON(%s) FROM %s LIMIT 100000",
                (AsIs(nameColumn), AsIs(self.name)))
            # ST_AsGeoJSON retourne une seule element par tuple
            self.geoJSonTab = []
            row = cursor.fetchone()
            while row is not None:
                self.geoJSonTab.append(row[0])
                row = cursor.fetchone()
            tpsFinJSon = time.clock()
            print( "Temps sur JSON :" + str( tpsFinJSon - tpsdebJSon))


###Layer for a Shapefile
class LayerShape:
    def __init__(self, cursor, name):
        self.name = name
        ds = DataSource(self.name)
        # shapefiles are only allowed to have one layer
        lyr = ds[0]
        

