from django.shortcuts import render, redirect
from .forms import MoodLogForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

# @login_required
def log_mood(request):
    if request.method == 'POST':
        form = MoodLogForm(request.POST)
        if form.is_valid():
            mood_log = form.save(commit=False)
            mood_log.user = request.user
            mood_log.save()
            return redirect('mood_history')
    else:
        form = MoodLogForm()
    return render(request, 'core/log_mood.html', {'form': form})
