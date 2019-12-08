from django.shortcuts import render, redirect
from .models import Squirrel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SqForm
from django.db.models import Avg, Max, Min, Count

def sightings_list(request):
    squirrels = Squirrel.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(squirrels, 20)
    try:
    	numbers = paginator.page(page)
    except PageNotAnInteger:
    	numbers = paginator.page(1)
    except EmptyPage:
    	numbers = paginator.page(paginator.num_pages)
    return render(request,'sightings/list.html',{'numbers':numbers})

def update(request, Unique_Squirrel_ID):
    sq = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SqForm(request.POST, instance=sq)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
        #check data with form
    else:
        form = SqForm(instance=sq)
        #build empty form

    context = {
        'form':form,
    }

    return render(request,'sightings/update.html',context)

def add(request):
    if request.method == 'POST':
        form = SqForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/sightings/add')
        #check data with form
    else:
        form = SqForm()
        #build empty form
    context = {
        'form':form,
    }
    return render(request,'sightings/add.html',context)

def stats(request):
    squirrels = Squirrel.objects.all()
    total = len(squirrels)
    latitude = squirrels.aggregate(minimum=Min('Latitude'), maximum=Max('Latitude'))
    longitude = squirrels.aggregate(minimum=Min('Longitude'), maximum=Max('Longitude'))
    foraging = squirrels.values_list('Foraging').annotate(Count('Foraging'))
    chasing = squirrels.values_list('Chasing').annotate(Count('Chasing'))
    eating = squirrels.values_list('Eating').annotate(Count('Eating'))
    context = {'total': total,
               'lattitude': lattitude,
               'longitude': longitude,
               'foraging': foraging,
               'chasing': chasing,
               'eating': eating,
    }
    return render(request,'sightings/stats.html',context)
