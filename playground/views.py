from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Profile, Note

def dashboard(request):
    #This is the dashboard which functions as HOME
    #Here Form is going to collect the data if the NOTE is submitted
    
    form = NoteForm(request.POST or None)
    
    if request.method == 'POST':
        
        #If form will be valid, then we can save it easily
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("dashboard")
    
    #Here we render the data to home.html page to present the notes
    return render(request, "home.html", {"form": form})

