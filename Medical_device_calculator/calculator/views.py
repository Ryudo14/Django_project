from django.views.generic import ListView, TemplateView,\
    DetailView, UpdateView, DeleteView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy

from .models import Search, Devices, Select


class SearchResultsView(ListView):
    model = Search
    template_name = 'search/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Devices.objects.filter(
            Q(name__icontains=query) | Q(batch__icontains=query)
        )
        return object_list


class DevicesView(TemplateView):
    model = Devices
    template_name = 'home.html'


class DevicesListView(ListView):
    model = Devices
    template_name = 'devices_list.html'


class DevicesUpdateView(UpdateView):
    model = Devices
    template_name = 'devices_edit.html'
    fields = ('name', 'batch', 'date', 'quantity_in_pack', 'quantity_thing', 'packing_price', 'price_for_one')


class DevicesDeleteView(DeleteView):
    model = Devices
    template_name = 'devices_delete.html'
    success_url = reverse_lazy('home')


class DevicesCreateView(CreateView):
    model = Devices
    template_name = 'devices_new.html'
    fields = ('name', 'batch', 'date', 'quantity_in_pack', 'quantity_thing', 'packing_price', 'price_for_one')


class ResultView(ListView):
    model = Devices
    template_name = 'home.html'
    fields = 'result'

    def __init__(self, num1, num2, **kwargs):
        super().__init__(**kwargs)
        self.num1 = num1
        self.num2 = num2


name = 'result'

# def calculate(num1, num2):
#     result = int(num1) * int(num2)
#     return result
#
#
# def home(request):
#     if request.method == 'post':
#         num1 = request.POST['num1']
#         num2 = request.POST['num2']
#         result = calculate(num1, num2)
#         return render(request, 'home.html', {'result': result})
#     return render(request, 'home.html')
