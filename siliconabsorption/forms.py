from django import forms

class inputParameters(forms.Form):
    shading = forms.FloatField(label='Shading (%)', initial=2)
    arc_thickness = forms.FloatField(label='ARC thicness (au)', initial=80)
    texture = forms.BooleanField(label='Texture?', initial=False,required=False)
    alrear = forms.BooleanField(label='Al rear?', initial=False,required=False)

