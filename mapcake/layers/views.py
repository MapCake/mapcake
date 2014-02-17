from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from owslib.wms import WebMapService
from django.template import RequestContext
from models import Layers
from django.contrib.auth.models import User
from forms import LayersForm, TYPE_SOURCE, FIELD_TYPE
from structure import LayerServices, LayerTable
import psycopg2
from userena import views
from django.contrib.auth.decorators import login_required

# voir http://docs.django-fr.org/intro/tutorial04.html#intro-tutorial04


def layer_index(request):    
    """Access index of the layers"""
    
    latestSourceList = Layers.objects.all()
    return render(request, 
        'layers/index.html',
        {'latestSourceList': latestSourceList})


def layer_detail(request, source_id):
    """Acess detail of the  index source_id"""
    layer = Layers.objects.get(pk=source_id)
    wms = WebMapService(layer.url, version='1.1.1')
    lstLayers = list(wms.contents)
    backGround = lstLayers[0]
    tabCoor = computeLonLatLayer(layer.url)
    lon = tabCoor[0]
    lat = tabCoor[1]
    lstNamesLayers = layer.source.split(";")
    lstLayers = []
    for currentName in lstNamesLayers:
        lstLayers.append(LayerServices(wms, currentName))
    return render(request,
        'layers/detail.html',
        {'layer': layer,
        'lon': lon, 'lat': lat, 'backGround': backGround})


def layer_delete(request, source_id):
    source = Layers.objects.get(pk=source_id)
    source.delete()
    return redirect("/layers")


@login_required
def layer_add(request):
    formSource = LayersForm(request.POST or None)
    if (request.method == 'POST'):
       # print request.body
        # le formulaire n'est pas valide
        if (('save' in request.POST) and not (formSource.is_valid())):
            # un enregistrement a ete demande
            #print formSource.errors
            return render(request, 
                'layers/add.html',
                {'formSource': formSource, 'error_message': True},
                context_instance=RequestContext(request))
        if  ('EnvService' in request.POST):
            # on reaffiche le service
            return getLayersForService(request, formSource)
        else:
            if('EnvBase' in request.POST):
                return getLayersForDatabase(request, formSource)

            else:
                if ('save' in request.POST):
                    if (TYPE_SOURCE[2][0] in request.POST[FIELD_TYPE]):
                        return saveLayersForService(request, formSource)
    else:
        print "%s" % repr(formSource.errors)
        print request.body
    return render(request,
        'layers/add.html', {'formSource': formSource},
        context_instance=RequestContext(request))


def  saveLayersForService(request, formSource):
    """Save a layer from a service"""
    baliseLayer = 'layerSelected'
    lstLayersString = ""
    lstLayersString = ";".join(
        request.POST.getlist(baliseLayer))
    currentSource = formSource.save(commit=False)
    currentSource.source = lstLayersString
    currentSource.save()

    print "save successfull"
    return redirect("/layers")


def getLayersForService(request, formSource):
    """Get a layer from a service with url.
    Recreate the form t take care of that"""
    name = None
    lon = None
    lat = None
    url = request.POST['url']
    wms = WebMapService(url, version='1.1.1')
    lstLayersService = []
    for currentLayer in wms.contents:
        lstLayersService.append(LayerServices(wms, currentLayer))

    tabCoor = computeLonLatLayer(url)
    lon = tabCoor[0]
    lat = tabCoor[1]
    return render(request,
        'layers/add.html',
        {'formSource': formSource,
        'url': url, 'lstLayersService': lstLayersService,
        'name': name, 'lon': lon, 'lat': lat},
        context_instance=RequestContext(request))


def getLayersForDatabase(request, formSource):
    """
Return the layers from an access to a database
    """
    port = request.POST['port']
    host = request.POST['server']
    base = request.POST['base']
    userName = request.POST['username']
    password = request.POST['password']
    connect = psycopg2.connect(
        host=host, database=base, user=userName, port=port, password=password)
    lstLayersTable = []
    requestAllTables = \
        "SELECT tablename FROM pg_tables WHERE tablename !~ '^pg_';"
    cursor = connect.cursor()
    cursor.execute(requestAllTables)
    tables = cursor.fetchall()
    for currentNameTable in tables:
        currentTable = LayerTable(cursor, currentNameTable[0])
        if (currentTable.geoJSonTab is not None):
            lstLayersTable.append(currentTable)

    return render(request,
        'layers/add.html',
        {'formSource': formSource,
         'lstLayersTable': lstLayersTable},
        context_instance=RequestContext(request))


# retourne les longitudes et latitude extremes a partir d'une url
def computeLonLatLayer(url):
    """Get max and min latitudes and longitude from an url"""
    lon = None
    lat = None
    wms = WebMapService(url, version='1.1.1')
    lstLayers = list(wms.contents)
    lstLayers.remove(lstLayers[0])
    minX = 360
    minY = 360
    maxY = -360
    maxX = -360
    for couche in list(wms.contents):
        currentBound = wms[couche].boundingBoxWGS84
        minX = min(minX, currentBound[0])
        minY = min(minY, currentBound[1])
        maxX = max(maxX, currentBound[2])
        maxY = max(maxY, currentBound[3])
    lon = minX + (maxX - minX) / 2
    lat = minY + (maxY - minY) / 2
    return[lon, lat]
