from django.shortcuts import get_list_or_404, get_object_or_404, render

def index(request):
  return render(request, 'metro/metro.html')
