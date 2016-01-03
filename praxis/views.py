from django.views.generic import ListView

from .models import Section


class Home(ListView):
    """
    View for home.
    """
    model = Section
