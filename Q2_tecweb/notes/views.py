from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        memo = request.POST.get('memo')
        note = Note(memo = memo) # é um objeto
        note.save()
        return redirect('index')
    else:
        last_note = Note.objects.last()
        return render(request, 'notes/index.html', {'note': last_note})