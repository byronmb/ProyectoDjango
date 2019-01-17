from django import forms
from app.modelo.models import Cliente
from app.modelo.models import Cuenta

from app.modelo.models import Transaccion
from django.utils.translation import gettext as _
from app.modelo.models import Transferencia

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]
        error_messages = {
            'cedula': {
                'required': _(""),
                'unique': _("Esta cedula ya existe"),
            },
            'nombres': {
                'required': _(""),
            },
            'apellidos': {
                'required': _(""),
            },
            'genero':{
                'required': _(""),
            },
            'estadoCivil': {
                'required': _(""),
            },
            'fechaNacimiento': {
                'required': _(""),
            },
            'correo': {
                'required': _(""),
                'unique': _("Ya existe un cliente con este correo"),
            },
            'telefono': {
                'required': _(""),
            },
            'celular': {
                'required': _(""),
            },
            'direccion': {
                'required': _(""),
            }
        }

        labels = {
            "cedula": _("Cedula:"),
        }


class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = [ "tipoCuenta"]
        error_messages = {
            'tipoCuenta':{
                'required': _(""),
            }
        }

class FormularioTransaccion(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = [  "tipo", "valor", "descripcion"]
        error_messages = {
            'tipo': {
                'required': _(""),
            },
            'valor': {
                'required': _(""),
            },
            'descripcion': {
                'required': _(""),
            },
        }



class FormularioTransferencia(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ["valor", "descripcion"]
        error_messages = {
            'valor': {
                'required': _(""),
            },
            'descripcion': {
                'required': _(""),
            },
        }


