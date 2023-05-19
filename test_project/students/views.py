from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Students
from django.urls import reverse_lazy


class StudentsListView(ListView):
    model = Students
    template_name = 'home.html'
    context_object_name = 'all_students_list'


class StudentsCreateView(CreateView):
    model = Students
    template_name = 'students_new.html'
    fields = '__all__'


class StudentsUpdateView(UpdateView):
    model = Students
    template_name = 'students_edit.html'
    fields = '__all__'


class StudentsDeleteView(DeleteView):
    model = Students
    template_name = 'students_delete.html'
    success_url = reverse_lazy('home')


class StudentsDetailView(DetailView):
    model = Students
    template_name = 'students_detail.html'
