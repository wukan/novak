from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from display.models import Route

def index(request):
  return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, route_id):
  route = get_object_or_404(Route, link_id=route_id)
  return render_to_response('display/detail.html', {'route': route})
