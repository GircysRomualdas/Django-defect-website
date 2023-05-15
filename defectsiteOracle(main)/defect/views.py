from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q

from .models import Location, Type, Position, LocationType
from .forms import LocationForm, TypeForm, PositionForm, LocationTypeForm

from django import forms

# location view start
def allLocationsView(request):
    locations = Location.objects.all().values()
    type = Type.objects.all().values()
    locationType = LocationType.objects.all().values()  # temp 

    context = { 
        'locations': locations,
        'type': type,
        'locationType': locationType,  
        }

    return render(request, 'location/all.html', context)

def createLocationView(request):
    form = LocationForm()

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('defect:allLocationsView')
    
    context = {'form':form,}
    return render(request, 'location/create.html', context)

def updateLocationView(request, id):
    location = Location.objects.get(nID=id)
    form = LocationForm(instance=location)

    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('defect:allLocationsView')

    context = {
        'location': location, 
        'form':form,
        }
    return render(request, 'location/update.html', context)

def deleteLocationView(request, id):
    location = Location.objects.get(nID=id)

    if request.method == 'POST':
        location.delete()
        return redirect('defect:allLocationsView')

    context = {'location': location}
    return render(request, 'location/delete.html', context)

def searchLocationView(request):
    query = request.GET.get("q")
    locations = Location.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    ).values()
    context = { 'locations': locations, }
    return render(request, 'location/all.html', context)

# location view end

# type view start
def allTypesView(request):
    type = Type.objects.all().values()
    context = { 'type': type, }
    return render(request, 'type/all.html', context)

def createTypeView(request):
    form = TypeForm()

    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('defect:allTypesView')
    
    context = {'form':form,}
    return render(request, 'type/create.html', context)

def updateTypeView(request, id):
    type = Type.objects.get(nID=id)
    form = TypeForm(instance=type)

    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('defect:allTypesView')

    context = {'type': type, 'form':form,}
    return render(request, 'type/update.html', context)

def deleteTypeView(request, id):
    type = Type.objects.get(nID=id)

    if request.method == 'POST':
        type.delete()
        return redirect('defect:allTypesView')

    context = {'type': type}
    return render(request, 'type/delete.html', context)

def searchTypeView(request):
    query = request.GET.get("q")
    type = Type.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    ).values()
    context = { 'type': type, }
    return render(request, 'type/all.html', context)

# type view end

# position view start
def allPositionsView(request):
    position = Position.objects.all().values()
    context = { 'position': position, }
    return render(request, 'position/all.html', context)

def createPositionView(request):
    form = PositionForm()

    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('defect:allPositionsView')
    
    context = {'form':form,}
    return render(request, 'position/create.html', context)

def updatePositionView(request, id):
    position = Position.objects.get(nID=id)
    form = PositionForm(instance=position)

    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('defect:allPositionsView')

    context = {'position': position, 'form':form,}
    return render(request, 'position/update.html', context)

def deletePositionView(request, id):
    position = Position.objects.get(nID=id)

    if request.method == 'POST':
        position.delete()
        return redirect('defect:allPositionsView')

    context = {'position': position}
    return render(request, 'position/delete.html', context)

def searchPositionView(request):
    query = request.GET.get("q")
    position = Position.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    ).values()
    context = { 'position': position, }
    return render(request, 'position/all.html', context)

# position view end

# custom view start
def customView(request):
    locations = Location.objects.all().values()
    type = Type.objects.all().values()
    context = { 
        'locations': locations, 
        'type': type,
        }
    return render(request, 'custom/custom.html', context)

def custom2View(request):
    locations = Location.objects.all().values()
    type = Type.objects.all().values()
    locationType = LocationType.objects.all().values()
    context = { 
        'locations': locations, 
        'type': type,
        'locationType': locationType,
        }
    return render(request, 'custom/custom2.html', context)

# custom view end






