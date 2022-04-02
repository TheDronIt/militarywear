from django.shortcuts import render, redirect
import random
from .models import *

def index(request):
	data = {

	}
	return render(request, 'page/index.html', data)
