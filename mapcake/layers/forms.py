from django.forms import ModelForm, Select, TextInput
from models import Layers


TYPE_SOURCE = (
    ('file', 'File'),
    ('bdd', 'B.B.D.D.'),
    ('services', 'Services'))

FIELD_TYPE = 'type'


class LayersForm(ModelForm):
    class Meta:
        model = Layers
        widgets = {
            'type': Select(
            choices=TYPE_SOURCE, attrs={'onchange': 'javascript:Affiche()'}),
            'url': TextInput}
