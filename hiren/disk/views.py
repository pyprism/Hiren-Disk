from django.shortcuts import render , render_to_response
from .models import Disk, Box
# Create your views here.


def index(request):
    return render_to_response('index.html')