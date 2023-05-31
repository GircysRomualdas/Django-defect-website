from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

from django import forms

# location view start

PER_PAGE = 10

from django.core.paginator import Paginator

def allLocationsView(request):
    locations = Location.objects.all()
    paginator = Paginator(locations, PER_PAGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 
        'page_obj': page_obj,
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

    paginator = Paginator(locations, PER_PAGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 
        'query': query,
        'page_obj': page_obj,
        }

    return render(request, 'location/all.html', context)

# start location assign type
def searchAssignLocationTypeView(request, id):
    location = Location.objects.get(nID=id)
    assigned = LocationType.objects.filter(nLocationID=id).values_list('nTypeID', flat = True)

    query = request.GET.get("q")
    type = Type.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    )
    paginator = Paginator(type, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'location': location,
        'lid': id,
        'page_obj': page_obj,
        'assigned': assigned,
        'query': query,
        }
    return render(request, 'location/assign_type.html', context)

def assignLocationTypeView(request, id):
    location = Location.objects.get(nID=id)
    type = Type.objects.all()

    assigned = LocationType.objects.filter(nLocationID=id).values_list('nTypeID', flat = True)

    paginator = Paginator(type, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'location': location,
        'lid': id,
        'page_obj': page_obj,
        'assigned': assigned,
        }
    return render(request, 'location/assign_type.html', context)

def addLocationTypeView(request, lid, tid):
    assigned = LocationType.objects.filter(nLocationID=lid).values_list('nTypeID', flat = True)
    if tid in assigned:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    locationType = LocationType()
    locationType.nLocationID = Location.objects.get(nID=lid)
    locationType.nTypeID = Type.objects.get(nID=tid)
    locationType.nHidden = 0

    locationType.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def removeLocationTypeView(request, lid, tid):
    assigned = list(LocationType.objects.filter(nLocationID=lid).values_list('nTypeID', flat = True))
    if assigned.count(tid) == 1 :
        locationType = LocationType.objects.get(nLocationID=lid, nTypeID=tid)
        locationType.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# end location assign type

# start location assign parent
def searchAssignLocationParentView(request, id):
    location = Location.objects.get(nID=id)

    query = request.GET.get("q")
    locations = Location.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    ).exclude(nID=id)
    paginator = Paginator(locations, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'location': location,
        'page_obj': page_obj,
        'query': query,
        }
    return render(request, 'location/assign_parent.html', context)

def assignLocationParentView(request, id):
    location = Location.objects.get(nID=id)
    locations = Location.objects.all().exclude(nID=id)
    paginator = Paginator(locations, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'location': location,
        'page_obj': page_obj,
        }
    return render(request, 'location/assign_parent.html', context)

def addLocationParentView(request, lid, parentid):
    location = Location.objects.get(nID=lid)
    location.nParentID = Location.objects.get(nID=parentid)
    location.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def removeLocationParentView(request, lid):
    location = Location.objects.get(nID=lid)
    location.nParentID = None
    location.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# end location assign parent

# location view end

# type view start
def allTypesView(request):
    types = Type.objects.all()
    paginator = Paginator(types, PER_PAGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 
        'page_obj': page_obj, 
        }
    
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
    types = Type.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    ).values()

    paginator = Paginator(types, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = { 
        'query': query,
        'page_obj': page_obj,
        }
    return render(request, 'type/all.html', context)

# start type assign position

def assignTypePositionView(request, id):
    type = Type.objects.get(nID=id)
    position = Position.objects.all()

    assigned = TypePosition.objects.filter(nTypeID=id).values_list('nPositionID', flat = True)

    paginator = Paginator(position, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'type': type,
        'tid': id,
        'page_obj': page_obj,
        'assigned': assigned,
        }
    return render(request, 'type/assign_position.html', context)

def searchAssignTypePositionView(request, id):
    type = Type.objects.get(nID=id)
    assigned = TypePosition.objects.filter(nTypeID=id).values_list('nPositionID', flat = True)

    query = request.GET.get("q")
    position = Position.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    )

    paginator = Paginator(position, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'type': type,
        'tid': id,
        'page_obj': page_obj,
        'assigned': assigned,
        'query': query,
        }
    return render(request, 'type/assign_position.html', context)

def addTypePositionView(request, tid, pid):
    assigned = TypePosition.objects.filter(nTypeID=tid).values_list('nPositionID', flat = True)

    if pid in assigned:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    typePosition = TypePosition()
    typePosition.nTypeID = Type.objects.get(nID=tid)
    typePosition.nPositionID = Position.objects.get(nID=pid)
    typePosition.nHidden = 0
    typePosition.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def removeTypePositionView(request, tid, pid):
    assigned = list(TypePosition.objects.filter(nTypeID=tid).values_list('nPositionID', flat = True))

    if assigned.count(pid) == 1:
        typePosition = TypePosition.objects.get(nTypeID=tid, nPositionID=pid)
        typePosition.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# start type assign parent
def assignTypeParentView(request, id):
    type = Type.objects.get(nID=id)
    types = Type.objects.all().exclude(nID=id)
    paginator = Paginator(types, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'type': type,
        'page_obj': page_obj,
    }

    return render(request, 'type/assign_parent.html', context)

def searchAssignTypeParentView(request, id):
    type = Type.objects.get(nID=id)

    query = request.GET.get("q")
    types = Type.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    ).exclude(nID=id)
    paginator = Paginator(types, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'type': type,
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'type/assign_parent.html', context)

def addTypeParentView(request, tid, parentid):
    type = Type.objects.get(nID=tid)
    type.nParentID = Type.objects.get(nID=parentid)
    type.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def removeTypeParentView(request, tid):
    type = Type.objects.get(nID=tid)
    type.nParentID = None
    type.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# end type assign parent

#  type assign position

# type view end

# position view start
def allPositionsView(request):
    positions = Position.objects.all()
    paginator = Paginator(positions, PER_PAGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 
        'page_obj': page_obj, 
        }
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
    positions = Position.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    ).values()

    paginator = Paginator(positions, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 
        'query': query,
        'page_obj': page_obj,
        }
    
    return render(request, 'position/all.html', context)

def assignPositionParentView(request, id):
    position = Position.objects.get(nID=id)
    positions = Position.objects.all().exclude(nID=id)
    paginator = Paginator(positions, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'position': position,
        'page_obj': page_obj,
    }

    return render(request, 'position/assign_parent.html', context)

def searchAssignPositionParentView(request, id):
    position = Position.objects.get(nID=id)

    query = request.GET.get("q")
    positions = Position.objects.filter(
        Q(nID__icontains=query) | Q(sName__icontains=query) | Q(sDescription__icontains=query)
    ).exclude(nID=id)
    paginator = Paginator(positions, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'position': position,
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'position/assign_parent.html', context)

def addPositionParentView(request, pid, parentid):
    position = Position.objects.get(nID=pid)
    position.nParentID = Position.objects.get(nID=parentid)
    position.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def removePositionParentView(request, pid):
    position = Position.objects.get(nID=pid)
    position.nParentID = None
    position.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# position view end 







