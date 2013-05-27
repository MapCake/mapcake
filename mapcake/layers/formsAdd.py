from django.forms import ModelForm, Select, TextInput
from models import Layers, Sources


class LayersForm(ModelForm):
    class Meta:
        model = Layers

TYPE_SOURCE = (
    ('file', 'File'),
    ('bdd', 'B.B.D.D.'),
    ('services', 'Services'))


class SourcesForm(ModelForm):
    class Meta:
        model = Sources
        widgets = {
            'type': Select(
            choices=TYPE_SOURCE, attrs={'onchange': 'javascript:Affiche()'}),
            'url': TextInput}
