from django.shortcuts import render, get_object_or_404, redirect
from .models import Apply
from django.utils import timezone
# Create your views here.
def home(request):
    applys = Apply.objects
    return render(request, 'home.html', {'applys':applys})

def detail(request, apply_id):
    apply_detail = get_object_or_404(Apply, pk=apply_id)
    return render(request, 'detail.html', {'apply_detail':apply_detail})

def create(request):
    return render(request, 'create.html')

def create_apply(request):
    apply = Apply()
    apply.name = request.GET['name']
    apply.age = request.GET['age']
    apply.say = request.GET['say']
    apply.gender = request.GET['gender']
    apply.pub_date = timezone.datetime.now()
    apply.save()
    return redirect('/detail/'+str(apply.id))

def read(request):
    applys = Apply.objects
    return render(request, 'read.html',{'applys':applys})

def edit(request, apply_id):
    edit_apply = Apply.objects.get(id = apply_id)
    return render(request, 'edit.html', {'apply': edit_apply})

def update(request, apply_id):
    update_apply = Apply.objects.get(id = apply_id)
    update_apply.name = request.GET['name']
    update_apply.age = request.GET['age']
    update_apply.say = request.GET['say']
    update_apply.gender = request.GET['gender']
    update_apply.pub_date = timezone.datetime.now()
    update_apply.save()
    return redirect('/detail/'+str(update_apply.id))

def delete(reqeust, apply_id):
    delete_apply = Apply.objects.get(id = apply_id)
    delete_apply.delete()
    return redirect('read')