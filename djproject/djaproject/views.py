from django.shortcuts import render, redirect
from .models import Note

# Create your views here.

def notes_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'djaproject/notes_list.html', {'notes': notes})

def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)
        return redirect('notes_list')
    return render(request, 'djaproject/add_note.html')
