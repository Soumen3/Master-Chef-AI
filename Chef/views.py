from django.shortcuts import render, redirect
from django.views import View
from .form import chefForm
from .AI import ask_chef_ai

# Create your views here.
class HomeView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		context['form'] = chefForm()
		
		context['recipe'] = request.session.get('recipe',"")
		
			
		return render(request, 'home.html', context)
	
	
	def post(self, request, *args, **kwargs):
		form = chefForm(request.POST)
		if form.is_valid():
			prompt = form.cleaned_data['prompt']
			recipe = ask_chef_ai(prompt)
			request.session['recipe'] = recipe
		return redirect('home')
		

