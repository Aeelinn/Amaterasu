from django import forms
import re
from Inventario.models import Material, Aula, Edificio, Marca, Tipo


class Validaciones():
    def clean(self):
        form_data = dict(self.cleaned_data)

        # \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
        regex = re.compile("\w")

        for data in form_data.values():
            data = str(data)
            if len(data) != 0:
                if not re.match(regex, data):
                    raise forms.ValidationError("El formulario contiene caracteres no válidos")

        return form_data


class LoginForm(Validaciones, forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class MaterialForm(Validaciones, forms.ModelForm):
    class Meta:
        model = Material


class AulaForm(Validaciones, forms.ModelForm):
    class Meta:
        model = Aula


class EdificioForm(Validaciones, forms.ModelForm):
    class Meta:
        model = Edificio


class MarcaForm(Validaciones, forms.ModelForm):
    class Meta:
        model = Marca


class TipoForm(Validaciones, forms.ModelForm):
    class Meta:
        model = Tipo