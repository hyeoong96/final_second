from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse



from .models import One

def home(request):
    return render(request,'home.html')

def book(request):
    ones = One.objects.all()
    return render(request,'book.html',{'ones':ones})


def detail(request,one_id):
    one_detail = get_object_or_404(One, pk=one_id)
    return render(request,'detail.html', {'one': one_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    one = One()
    one.title = request.GET['title']
    one.body = request.GET['body']
    one.score = request.GET['score']
    one.pub_date = timezone.datetime.now()
    one.save()
    return redirect('/one/' + str(one.id))

