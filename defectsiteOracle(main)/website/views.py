from django.shortcuts import render, redirect

def homeView(request):
    context = {}
    return redirect('defect:allLocationsView')
