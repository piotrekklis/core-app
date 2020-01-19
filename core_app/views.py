from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import core_object
from .forms import core_object_form, edit_core_object_form

# Create your views here.
def index(request):
    return HttpResponse("Welcome. You're at the core_app index.")

def logged_out(request):
    return HttpResponse("Hope you enjoyed your stay @core_app. Bye!")

def add_core_object(request):
    if not request.user.is_authenticated:
        return HttpResponse("Sign in or register.")
    else:
        if request.method == 'POST':
            form = core_object_form(request.POST)
            if form.is_valid():
                if core_object.objects.filter(name = form.cleaned_data['name']).count() == 0:
                    new_core_object_name = form.cleaned_data['name']
                    new_core_object_width = form.cleaned_data['width']
                    new_core_object_height = form.cleaned_data['height']
                    new_core_object_weight = form.cleaned_data['weight']
                    new_core_object_save = core_object(name= new_core_object_name, width= new_core_object_width, height= new_core_object_height, weight= new_core_object_weight)
                    new_core_object_save.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    return HttpResponse("Object exists.")
        else:
            form = core_object_form()
        all_core_objects = core_object.objects.all()
        return render(request, 'add_core_object.html', {'form': form, 'all_core_objects': all_core_objects})

def edit_core_object(request, core_object_id):
    if not request.user.is_authenticated:
        return HttpResponse("Sign in or register.")
    else:
        instance = core_object.objects.get(id= core_object_id)
        form = edit_core_object_form(request.POST or None, instance= instance)
        if form.is_valid():
            form.save()
            return redirect(request.build_absolute_uri('/core_app/add_core_object/'))
        
        all_core_objects = core_object.objects.all()
        return render(request, 'edit_core_object.html', {'form': form, 'all_core_objects': all_core_objects})
