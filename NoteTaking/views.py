from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.shortcuts import get_list_or_404
# Create your views here.
def note_index(request):
    notes = Note.objects.all()
    return render(request, 'note_index.html', {'notes':notes})

def note_add(request):
    if request.method == 'POST':
        note = Note(
            title = request.POST.get('title'),
            description = request.POST.get('description')
        )
        note.save()
        return redirect('note_index')
    return render(request,'note_add.html')

def note_edit(request, title):
    try:
        if title.isnumeric():
            note = Note.objects.get(id = title)
        else:
            note = Note.objects.get(title = title)
        if request.method == 'POST':
            note.title = request.POST.get('title')
            note.description = request.POST.get('description')
            note.date_created = datetime.now()
            note.save()
            return redirect('note_index')
        return render(request, 'note_edit.html', {'note':note})
    except Note.MultipleObjectsReturned:
        note = get_list_or_404(Note, title = title)
        return render(request,'note_edit.html', {'note':note})

def note_delete(request, id):
    note = Note.objects.get(id = id)
    note.delete()
    return redirect('note_index')