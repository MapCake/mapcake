
Installer python 2.7.4
Installer virtualEnv
Creer un environnement virtuel (commande virtulenv mapcake)
Activer l'environnement virtuel en lançant le script activate du sous dossier bin du dossier de l'environnement
A l'aide de la commande pip install nomPackage, installer les packages suivants:
dateutil                       pip-1.1-py2.7.egg
distribute-0.6.24-py2.7.egg    pip-1.3.1-py2.7.egg
distribute-0.6.34-py2.7.egg    psycopg2
django                         psycopg2-2.4.6-py2.7.egg-info
Django-1.5-py2.7.egg-info      python_dateutil-2.1-py2.7.egg-info
easy-install.pth               pytz
ipdb                           pytz-2012j-py2.7.egg-info
ipdb-0.7-py2.7.egg-info        setuptools.pth
IPython                        six-1.3.0-py2.7.egg-info
ipython-0.13.1-py2.7.egg-info  six.py
owslib                         six.pyc
OWSLib-0.7.1-py2.7.egg-info    tests
pep8-1.4.5-py2.7.egg-info      yolk
pep8.py                        yolk-0.4.3-py2.7.egg-info
gdal



Mettre à jour le contenu de la balise DATABASES du fichier mapCake\mapCake\settings.py.

Se placer dans le dossier mapCake et lancer la commande  python manage.py syncdb (installation de la base) puis python manage.py runserver (création du serveur).
Point d'entrée pour tester les sources:
http://localhost:8000/sources/index
