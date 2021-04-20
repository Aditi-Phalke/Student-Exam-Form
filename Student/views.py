from django.shortcuts import render, redirect
from .forms import Contact
from .forms import StudentForm
def welcome(request):
    return render(request, "welcome.html")

def load_form(request):
    form=StudentForm
    return render(request, "index.html", {'form':form})

def add(request):
    form=StudentForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    contact=Contact.objects.all()
    return render(request, 'show.html', {'contact':contact})

def edit(request, usn):
    contact=Contact.objects.get(usn=usn)
    return render(request, 'edit.html', {'contact':contact})

def update(request, usn):
    contact=Contact.objects.get(usn=usn)
    form=StudentForm(request.POST, instance=contact)
    form.save()
    return redirect('/show')

def delete(request, usn):
    contact = Contact.objects.get(usn=usn)
    contact.delete()
    return redirect('/show')

def search(request):
    given_name=request.POST['name']
    contact = Contact.objects.filter(name__icontains=given_name)
    return render(request, 'show.html', {'contact':contact})



