from django.shortcuts import render

# Create your views here.
 def index_temario(request):
     return_render(request,template_name="temario/index.html")
