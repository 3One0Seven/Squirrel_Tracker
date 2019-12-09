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
    longitude = squirrels.aggregate(minimum=Min('X'), maximum=Max('X'))
    latitude = squirrels.aggregate(minimum=Min('Y'), maximum=Max('Y'))
    shift = squirrels.values_list('Shift').annotate(Count('Shift'))
    running = squirrels.values_list('Running').annotate(Count('Running'))
    eating = squirrels.values_list('Eating').annotate(Count('Eating'))
    context = {'total': total,
               'latitude': latitude,
               'longitude': longitude,
               'AM': shift[0][1],
               'PM': shift[1][1],
               'Is_Running': running[1][1],
               'Not_Running': running[0][1],
               'Is_Eating': eating[1][1],
               'Not_Eating': eating[0][1],
    }
    return render(request,'sightings/stats.html',context)
