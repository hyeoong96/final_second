from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse



from .models import Two
def movie(request):
    twos = Two.objects.all()
    return render(request,'movie.html',{'twos':twos})


def detailm(request,two_id):
    two_detail = get_object_or_404(Two, pk=two_id)
    return render(request,'detailm.html', {'two': two_detail})

def newm(request):
    return render(request,'newm.html')

def createm(request):
    two = Two()
    two.title = request.GET['title']
    two.body = request.GET['body']
    two.score = request.GET['score']
    two.pub_date = timezone.datetime.now()
    two.save()
    return redirect('/two/' + str(two.id))