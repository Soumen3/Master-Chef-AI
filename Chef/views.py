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
		context['error'] = request.session.pop('error', "")  # Get and remove error from session
		
		return render(request, 'Home.html', context)
	
	
	def post(self, request, *args, **kwargs):
		form = chefForm(request.POST)
		if form.is_valid():
			prompt = form.cleaned_data['prompt']
			recipe = ask_chef_ai(prompt)
			if recipe.startswith("ERROR:"):
				request.session['error'] = recipe.replace("ERROR:", "").strip()
				request.session['recipe'] = ""
			else:
				request.session['recipe'] = recipe
				request.session['error'] = ""
		return redirect('home')


