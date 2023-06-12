from django import forms
from django.forms import ModelForm
from .models import Modifiche, Artista, Collezione, Opera


class ModificheForm(ModelForm):
	class Meta:
		model = Modifiche
		fields = "__all__"


class ArtistaFormAdmin(ModelForm):
	class Meta:
		model = Artista
		fields = "__all__"

class ArtistaForm(ModelForm):
	class Meta:
		model = Artista
		fields = ('biografia', )


class OperaForm(ModelForm):
	class Meta:
		model = Opera
		fields = "__all__"


class CollezioneFormAdmin(ModelForm):
	class Meta:
		model = Collezione
		fields = "__all__"


class CollezioneForm(ModelForm):
	class Meta:
		model = Collezione
		fields = ('nominativo', 'info', 'opera', )