# encoding: utf-8

from django.shortcuts import (render, get_object_or_404, redirect, render_to_response)
from django.http import HttpResponseRedirect
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.core.paginator import (Paginator, PageNotAnInteger,EmptyPage)
from django.views.generic import View, ListView, DetailView

from models import Rhythm, DanceStep
from forms import DanceStepForm, RhythmForm


class RhythmListView(ListView):

	template_name = 'dances/index.html'
	paginate_by = 1

	def get_queryset(self):
		rhythms = Rhythm.objects.all()
		search = self.request.GET.get('search', '')
		if search:
			rhythms = rhythms.filter(Q(name__icontains=search) 
			     				   | Q(description__icontains=search))
		return rhythms

	def get_context_data(self, **kwargs):
		context = super(RhythmListView, self).get_context_data(**kwargs)
		context['search'] = self.request.GET.get('search', '')
		return context

### usado como base

def sorted(request):
	return render_to_response('dances/sortedsteps.html')


# def dancestep_sorted(request, pk):
# 	rhythm = get_object_or_404(Rhythm, pk=pk)
# 	template_name = 'dances/sortedsteps.html'
# 	rhythm_slug = self.kwargs.get('slug')
#    	rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
# 	items = list( rhythm.dancesteps.all().order_by('?')[:1])
#   	return items


def index_ds(request):
	template_name = 'dances/index_ds.html'
	context = {}
	dancesteps = DanceStep.objects.all()
	context['dancesteps'] = dancesteps
	return render(request, template_name, context)


class RhythmDetailView(DetailView):

	template_name = 'dances/details.html'
	context_object_name = 'rhythm'

	def get_queryset(self):
		if not request.user.is_authenticated():
			return Rhythm.objects.filter(public=True)
		return Rhythm.objects.all()

	def get_context_data(self, **kwargs):
		context = super(RhythmDetailView, self).get_context_data(**kwargs)
		form = DanceStepForm(self.request.POST or None)
		context['dancestep_form'] =  form
		return context

	def post(self, request, pk):
		self.object = self.get_object()
		context = self.get_context_data()
		form = context['dancestep_form']
		if form.is_valid():
			dancestep = form.save(commit=False)
			dancestep.rhythm = self.object
			dancestep.save()
			return redirect('rhythms_details', rhythm.pk)
		return self.render_to_response(context)





def details(request, pk):
	rhythm = get_object_or_404(Rhythm, pk=pk)
	template_name = 'dances/details.html'
	if not rhythm.public and not request.user.is_authenticated:
		return redirect_to_login(request.path)
	if request.method == 'POST':
		form = DanceStepForm(request.POST)
		if form.is_valid():
			dancestep = form.save(commit=False)
			dancestep.rhythm = rhythm
			dancestep.save()
			return redirect('rhythms_details', rhythm.pk)
	else:
		form = DanceStepForm()

	context = {
		'rhythm':rhythm,
		'dancestep_form':form,
	}
	return render(request, template_name, context)

def steps_by_rhytm(request, slug):
	step = get_object_or_404(DanceStep, slug=slug)
	template_name = 'dances/step_rhythm.html'
	context = {
		'step':step,
	}
	return render(request, template_name, context)

def dancestep_sorted(request, pk):
	rhythm = get_object_or_404(Rhythm, pk=pk)
	template_name = 'dances/sortedsteps.html'
	rhythm_slug = rhythm.slug
   	rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
	items = list(rhythm.dancesteps.all().order_by('?')[:1])
	context = {
		'items':items,
	}
  	return render(request, template_name, context)

@login_required
def create(request):
	template_name = 'dances/create.html'
	context = {}
	if request.method == 'POST':
		form = RhythmForm(request.POST)
		if form.is_valid():
			rhythm = form.save(commit=False)
			rhythm.user = request.user
			rhythm.save()
			next_url = rhythm.get_absolute_url()
			return HttpResponseRedirect(next_url)
	else:
		form = RhythmForm()
	context['form'] = form
	return render(request, template_name, context)


@login_required
def my(request):
	template_name = 'dances/my.html'
	context = {}
	rhythms = Rhythm.objects.filter(user=request.user)
	paginator = Paginator(rhythms, 3)
	page = request.GET.get('page', 1)
	try:
		page_obj = paginator.page(page)
	except PageNotAnInteger:
		page_obj = paginator.page(1)
	except EmptyPage:
		page_obj = paginator.page(paginator.num_pages)
	
	context['page_obj'] = page_obj
	context['paginator'] = paginator
	context['rhythms'] = rhythms
	return render(request, template_name, context)

@login_required
def edit(request,pk):
	template_name = 'dances/edit.html'
	rhythm = get_object_or_404(Rhythm, pk=pk,
							   user=request.user)
	context = {}
	context['rhythm'] = rhythm
	if request.method == 'POST':
		form = RhythmForm(data=request.POST, instance=rhythm)
		if form.is_valid():
			form.save()
			return redirect('rhythm_my')
	else:
		form = RhythmForm(instance=rhythm)
	context['form'] = form
	return render(request, template_name, context)

@login_required
def delete(request, pk):
	template_name = 'dances/delete.html'
	rhythm = get_object_or_404(Rhythm, pk=pk,
							   user=request.user)
	context['Rhythm'] = rhythm
	if request.method =='POST':
		rhythm.delete()
		return redirect('rhythm_my')
	context = {}
	context['rhythm'] = rhythm
	return render(request, template_name, context)