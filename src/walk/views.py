from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView, CreateView
from django import forms
from checkpoint.models import CheckPoint
from .models import *
from django.template.context_processors import csrf


class SearchForm(forms.Form):
	description = forms.CharField(required=False, label=False)
	categories = forms.MultipleChoiceField(
choices=(('feet', 'пешые'),
        ('bikes', 'велосипедные'),
        ('rollers', 'на роликах'),
        ('other', 'другие'),), required=False, label=False)

	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'GET'
		self.helper.layout = Layout(
			Field("description", placeholder="Поиск прогулок по описанию"),
			InlineCheckboxes('categories'), )
		self.helper.add_input(Submit('submit', 'Искать'))

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ('modified_at', 'created_at', 'user', 'walk')
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'GET'
		self.helper.layout = Layout(
			Field("text", placeholder="Введите комментарий"),)
		self.helper.add_input(Submit('submit', 'Отправить'))

class LikeForm(forms.ModelForm):
	class Meta:
		model = Like
		exclude = ('modified_at', 'created_at', 'user', 'walk')
@require_POST
def add_comment(request, walk_id):
	form = CommentForm(request.POST or None)
	walk = get_object_or_404(Walk, id=walk_id)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.user = request.user
		comment.walk = walk
		comment.save()
		return redirect('walks:walk_detail', walk.pk)
	print("Нет зарегистрирован был")
	return render(request, 'walk/walk_detail.html',
				 {'form':form, 'walk': walk})
@require_POST
def add_like(request, walk_id):
	print('Hello')
	form = LikeForm(request.POST or None)
	walk = get_object_or_404(Walk, id=walk_id)
	if not Like.objects.filter(user=request.user, walk=walk):
		like = Like(user=request.user, walk=walk, isLike=1)
		like.save()
	return redirect('walks:walk_detail', walk.pk)
	##print("Нет зарегистрирован был")
	#return render(request, 'walk/walk_detail.html',
	#			 {'form':form, 'walk': walk})
@require_POST
def delete_comment(request, walk_id, comment_id):
	walk = get_object_or_404(Walk, id=walk_id)
	comment = get_object_or_404(Comment, id=comment_id, walk_id=walk_id)
	comment.delete()
	return redirect('walks:walk_detail', walk.pk)

def filter(request, type_of_move):
	template_name = 'walk/walks_list.html'
	print(type_of_move)
	queryset = Walk.objects.filter(type_of_move = type_of_move)
	print(queryset)
	return render(request = request, template_name= template_name,
				  context = {'object_list': queryset})

class WalkList(ListView):
	template_name = 'walk/walks_list.html'
	queryset = Walk.objects.all()
	paginate_by = 10

	def dispatch(self, request, *args, **kwargs):
		self.searchform = SearchForm(request.GET)
		return super(WalkList, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(WalkList, self).get_context_data(**kwargs)
		context['form'] = self.searchform
		return context

	def get_queryset(self):
		if self.searchform.is_valid():
			searchstring = self.searchform.cleaned_data['description']
			search_move_type = self.searchform.cleaned_data['categories']
			if search_move_type:
				return Walk.objects.filter(description__icontains = searchstring,
										   type_of_move__in = search_move_type)
			else:
				return Walk.objects.filter(description__icontains=searchstring)
		return Walk.objects.order_by('modified_at')

class WalkView(DetailView):
	template_name = 'walk/walk_detail.html'
	queryset = Walk.objects.all()

	def get_context_data(self, **kwargs):
		context = super(WalkView, self).get_context_data(**kwargs)
		form = CommentForm()
		context['form'] = form
		return context
