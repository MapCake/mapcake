from django.shortcuts import render_to_response, redirect
from owslib.wms import WebMapService
from django.template import RequestContext
from models import Sources, Users
from formsAdd import LayersForm, SourcesForm
from structure import LayerServices

# voir http://docs.django-fr.org/intro/tutorial04.html#intro-tutorial04


def source_index(request):
    latestSourceList = Sources.objects.all()
    return render_to_response(
        'sources/index.html',
        {'latestSourceList': latestSourceList})


def source_detail(request, source_id):
    source = Sources.objects.get(pk=source_id)
    wms = WebMapService(source.url, version='1.1.1')
    lstLayers = list(wms.contents)
    fondDePlan = lstLayers[0]
    tabCoor = calculLonLatLayer(source.url)
    lon = tabCoor[0]
    lat = tabCoor[1]
    lstNamesLayers = source.source.split(";")
    lstLayers = []
    for currentName in lstNamesLayers:
        lstLayers.append(LayerServices(wms, currentName))
    return render_to_response(
        'sources/detail.html',
        {'source': source, 'lstLayers': lstLayers,
        'lon': lon, 'lat': lat, 'fondDePlan': fondDePlan})


def source_delete(request, source_id):
    source = Sources.objects.get(pk=source_id)
    source.delete()
    return redirect("/sources/index")


def layer_add(request):
    formLayer = LayersForm(request.POST or None)
    if formLayer.is_valid():
        currentLayer = formLayer.save(commit=False)
        currentLayer.source = Sources.objects.get(id=1)
        currentLayer.user = Users.objects.get(id=1)
        currentLayer.save()
        return redirect(currentLayer)
    return render_to_response(
        'layers/add.html', {'formLayer': formLayer},
        context_instance=RequestContext(request))


def source_add(request):
    formSource = SourcesForm(request.POST or None)
    if (request.method == 'POST'):
       # print request.body
        # le formulaire n'est pas valide
        if (('enregistrer' in request.POST) and not (formSource.is_valid())):
            # un enregistrement a ete demande
            #print formSource.errors
            return render_to_response(
                'sources/add.html',
                {'formSource': formSource, 'error_message': True},
                context_instance=RequestContext(request))
        if not ('enregistrer' in request.POST):
            return getLayersForSource(request, formSource)
    if (formSource.is_valid() and
        (request.method == 'POST') and
        ('enregistrer' in request.POST)):
        print "formulaire valide"
        #enregistrement des sources
        baliseLayer = 'layerSelected'
        #print request.body
        lstLayersString = ""
        if (baliseLayer in request.POST):
            # a reprendre chercher django checkbox
            lstLayersString = ";".join(request.POST.getlist(baliseLayer))
        currentSource = formSource.save(commit=False)
        currentSource.source = lstLayersString
        currentSource.save()
        return redirect("/sources/index")
    else:
        print "%s" % repr(formSource.errors)
        print request.body
    return render_to_response(
        'sources/add.html', {'formSource': formSource},
        context_instance=RequestContext(request))


# recupere les layers pour une source a l'aide l'url de la requete
#Regenere le formulaire formSource pour en tenir compte
def getLayersForSource(request, formSource):
    name = None
    lon = None
    lat = None
    url = request.POST['url']
    # url = 'http://www.cartociudad.es/wms/CARTOCIUDAD/CARTOCIUDAD?'
    wms = WebMapService(url, version='1.1.1')
    lstLayers = []
    for currentLayer in wms.contents:
        lstLayers.append(LayerServices(wms, currentLayer))

    fondDePlan = lstLayers[0]
    tabCoor = calculLonLatLayer(url)
    lon = tabCoor[0]
    lat = tabCoor[1]
    return render_to_response(
        'sources/add.html',
        {'formSource': formSource,
        'url': url, 'lstLayers': lstLayers, 'fondDePlan': fondDePlan,
        'name': name, 'lon': lon, 'lat': lat},
        context_instance=RequestContext(request))


# retourne les longitudes et latitude extremes a partir d'une url
def calculLonLatLayer(url):
    lon = None
    lat = None
    # url = 'http://www.cartociudad.es/wms/CARTOCIUDAD/CARTOCIUDAD?'
    wms = WebMapService(url, version='1.1.1')
    lstLayers = list(wms.contents)
    lstLayers.remove(lstLayers[0])
    # TODO faire une structure
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
