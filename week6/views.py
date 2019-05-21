from django.shortcuts import render, redirect
from .models import Message


# Create your views here.
def home(request):
    messages = Message.objects
    return render(request, 'home.html', {'messages': messages})

def submit(request):
    m = Message()
    m.content = request.GET['saving']
    m.date=request.GET['date']
    m.writer=request.GET['writer']
    m.save()
    return redirect('/')

def delete(request):
    c = Message.objects.writer
    c.delete()
    return redirect('/')
