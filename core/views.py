from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
	count = User.objects.count()
	return render(request,"home.html",{
			'count':count,
		})


def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = UserCreationForm()
	context = {
		'form':form
	}
	return render(request, "registration/signup.html",context)

@login_required
def secret(request):
	return render(request,"secret.html", {})


class SecretView(LoginRequiredMixin,TemplateView):
	template_name = "secret.html"