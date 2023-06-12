from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy  
from .models import Artista, Opera, Collezione, Modifiche
from .forms import ModificheForm, ArtistaForm, CollezioneForm, OperaForm, ArtistaFormAdmin, CollezioneFormAdmin

# Create your views here.
def homePageView(request):
	return render(request, 'mostra/home.html')


class OperaListView(ListView):
	model = Opera
	template_name = "mostra/opera_list.html"


class OperaDetailView(DetailView): 
    model = Opera
    template_name = "mostra/opera_detail.html"



class ArtistaListView(ListView):
	model= Artista
	template_name="mostra/artista_list.html"

class ArtistaDetailView(DetailView):
	model= Artista
	template_name= "mostra/artista_detail.html"


class CollezioneListView(ListView):
	model= Collezione
	template_name="mostra/collezione_list.html"

class CollezioneDetailView(DetailView):
	model= Collezione
	template_name= "mostra/collezione_detail.html"



def add_modifiche(request):
	submitted= False
	if request.method == "POST":
		form= ModificheForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contattaci?submitted=True')
	else:
		form = ModificheForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'mostra/add_modifiche.html', {'form':form, 'submitted': submitted})


def add_artista(request):
	submitted= False
	if request.method == "POST":
		if request.user.is_superuser:
			form= ArtistaFormAdmin(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/add_artista?submitted=True')
		else:
			form = ArtistaForm(request.POST)
			if form.is_valid():
				artista = form.save(commit=False)
				artista.nome = request.user.username
				artista.save()
				return HttpResponseRedirect('/add_artista?submitted=True')
	else:
		form = ArtistaForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'mostra/add_artista.html', {'form':form, 'submitted': submitted})

def add_collezione(request):
	submitted= False
	if request.method == "POST":
		if request.user.is_superuser:
			form= CollezioneFormAdmin(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/add_collezione?submitted=True')
		else:
			form = CollezioneForm(request.POST)
			if form.is_valid():
				collezione = form.save(commit=False)
				collezione.proprietario = request.user.username
				collezione.save()
				return HttpResponseRedirect('/add_collezione?submitted=True')
	else:
		form = CollezioneForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'mostra/add_collezione.html', {'form':form, 'submitted': submitted})


def add_opera(request):
	submitted= False
	if request.method == "POST":
		form= OperaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_opera?submitted=True')
	else:
		form = OperaForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'mostra/add_opera.html', {'form':form, 'submitted': submitted})



def update_artista(request, artista_id):
	artista = Artista.objects.get(pk=artista_id)
	form = ArtistaForm(request.POST or None, request.FILES or None, instance=artista)
	if form.is_valid():
		form.save()
		return redirect('artista')

	return render(request, 'mostra/update_artista.html', {'artista': artista, 'form':form})

def update_collezione(request, collezione_id):
	collezione = Collezione.objects.get(pk=collezione_id)
	form = CollezioneForm(request.POST or None, request.FILES or None, instance=collezione)
	if form.is_valid():
		form.save()
		return redirect('collezione')

	return render(request, 'mostra/update_collezione.html', {'collezione': collezione, 'form':form})


def update_opera(request, opera_id):
	opera = Opera.objects.get(pk=opera_id)
	form = OperaForm(request.POST or None, request.FILES or None, instance=opera)
	if form.is_valid():
		form.save()
		return redirect('opera')

	return render(request, 'mostra/update_opera.html', {'opera': opera, 'form':form})


def deletesure_artista(request, artista_id):
	artista = Artista.objects.get(pk=artista_id)
	return render(request, 'mostra/deletesure_artista.html', {'artista': artista})

def delete_artista(request, artista_id):
	artista = Artista.objects.get(pk=artista_id)
	artista.delete()
	return redirect('artista')

def deletesure_collezione(request, collezione_id):
	collezione = Collezione.objects.get(pk=collezione_id)
	return render(request, 'mostra/deletesure_collezione.html', {'collezione': collezione})

def delete_collezione(request, collezione_id):
	collezione = Collezione.objects.get(pk=collezione_id)
	collezione.delete()
	return redirect('collezione')

def delete_opera(request, opera_id):
	opera = Opera.objects.get(pk=opera_id)
	opera.delete()
	return redirect('opera')




def search_artista(request):
	if request.method == "POST":
		searched = request.POST['searched']
		artista = Artista.objects.filter(nome__contains=searched)
		return render(request, 'mostra/search_artista.html', {'searched':searched, 'artista':artista})
	else:
		return render(request, 'mostra/search_artista.html', {})


def search_collezione(request):
	if request.method == "POST":
		searched = request.POST['searched']
		collezione = Collezione.objects.filter(nominativo__contains=searched)
		return render(request, 'mostra/search_collezione.html', {'searched':searched, 'collezione':collezione})
	else:
		return render(request, 'mostra/search_collezione.html', {})



def search_opera(request):
	if request.method == "POST":
		searched = request.POST['searched']
		opera = Opera.objects.filter(titolo__contains=searched)
		return render(request, 'mostra/search_opera.html', {'searched':searched, 'opera':opera})
	else:
		return render(request, 'mostra/search_opera.html', {})