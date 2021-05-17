from apply.forms import CreateApplyForm
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
    if request.method == 'POST':
        form = CreateApplyForm(request.POST)
        if form.is_valid():
            apply = form.save(commit=False)
            apply.pub_date = timezone.datetime.now()
            apply.save()
        return redirect('/detail/'+str(apply.id))
    else:
        form = CreateApplyForm()
    return render(request, 'create.html', {'form':form})

def read(request):
    applys = Apply.objects
    return render(request, 'read.html',{'applys':applys})

def edit(request, apply_id):
    edit_apply = Apply.objects.get(id = apply_id)
    return render(request, 'edit.html', {'apply': edit_apply})

def update(request, apply_id):
    apply = Apply.objects.get(id = apply_id)
    if request.method == "POST":
        form = CreateApplyForm(request.POST, instance = apply)
        if form.is_valid():
            apply = form.save()
            return redirect('/detail/'+str(apply.id))
    else:
        form = CreateApplyForm(instance=apply)
        return render(request, 'create.html', {'form':form})


def delete(reqeust, apply_id):
    delete_apply = Apply.objects.get(id = apply_id)
    delete_apply.delete()
    return redirect('read')