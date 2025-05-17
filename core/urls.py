from django.urls import path
from .views import home, log_mood

urlpatterns = [
    path('', home, name='home'),
    path('log-mood/', log_mood, name='log_mood'),
    # other paths...
]
