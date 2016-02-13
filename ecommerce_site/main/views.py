from django.shortcuts import render, render_to_response
from django.template import RequestContext


def index(request):
	"""Landing Page"""
	return render(request, 'main/index.html')