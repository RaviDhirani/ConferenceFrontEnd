from django.shortcuts import render, HttpResponse
from .models import ToDoItem, Objectives
# Create your views here.
def home(request):
    return render(request,"homeV5.0.html")

def form(request):
    return render(request,"form.html")

def objectives(request):
    items =Objectives.objects.all()

    return render(request,"objectives.html",{"objectives": items})
