from django.shortcuts import render

from .models import Table
from django.views.generic import ListView


class ListTable(ListView):
    model = Table
    template_name = 'home.html'
    context_object_name = 'all_table_list'

