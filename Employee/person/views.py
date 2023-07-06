from django.views.generic import ListView
from .models import Person


class PersonListView(ListView):
    template_name = 'person_list.html'
    model = Person
