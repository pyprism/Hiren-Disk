from django.shortcuts import render , render_to_response
from .models import Disk, Box
# Create your views here.


def index(request):
    return render_to_response('index.html', {'browse': "browse", "add": "x"})


def browse(request):
    no = Box.objects.values('disk_no', 'created_at')
    print(no)
    return render_to_response('browse.html', { 'no' : no})