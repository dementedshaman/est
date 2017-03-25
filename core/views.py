from django.urls import reverse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Analise, Classe, Data, Table
from django.urls import reverse_lazy

from django.contrib import messages

class AvaliationNew(CreateView):
    model = Analise
    fields = ['swCsvRi', 'titulo', 'csv', 'csvDel', 'csvQuo', 'rawinput', 'rawinputDel']
    template_name = 'core/create.html'

    def form_valid(self, form):
        self.object = form.save()
        if ( form.cleaned_data.get('swCsvRi', 1) == 1):
            self.object.saveCsv()
        else:
            self.object.saveRawInput()
        self.object.calcSturges()
        self.object.catClasses()
        self.object.constructTable()
        self.object.calcM()

        messages.add_message(
            self.request, messages.SUCCESS, 'Atividade submetida com sucesso!',
            fail_silently=True,
        )
        return redirect('/core/view/' + str(self.object.id ))

def index(request):
    analises = Analise.objects.all()

    return render(request, 'core/index.html', {
        'analises': analises,
    })

def view(request, id):
    analise = Analise.objects.get(pk=id)

    bar_graph_x_min = analise.classes.all().order_by('inicio').first().inicio
    bar_graph_x_max = analise.classes.all().order_by('-fim').first().fim
    bar_graph_y_min = analise.tables.all().order_by('fi').first().fi
    bar_graph_y_max = analise.tables.all().order_by('-fi').first().fi

    return render(request, 'core/view.html', {
        'analise': analise,
        'tables': analise.tables.all(),
        'data': analise.data.all(),
        'desvioCima': analise.media + analise.desvio,
        'desvioBaixo': analise.media - analise.desvio,
        'bar_graph_x_min': bar_graph_x_min,
        'bar_graph_x_max': bar_graph_x_max,
        'bar_graph_y_min': bar_graph_y_min,
        'bar_graph_y_max': bar_graph_y_max,
    })

def dataView(request, id):
    analise = Analise.objects.get(pk=id)

    return render(request, 'data/view.html', {
        'analise': analise,
        'data': analise.data.all().order_by('id'),
        'dmin': analise.data.order_by('id').first().id,
    })

class DataUpdate(UpdateView):
    model = Data
    fields = ['value']
    template_name = 'data/create.html'
    
    def get_object(self, queryset=None):
        obj = Data.objects.filter(id=self.kwargs['id']).first()
        return obj

    def get_success_url(self):
        return reverse('data-view', kwargs={'id': self.get_object().analise.id})
    
    # template_name_suffix = '_update_form'
# def dataCreate():

class dataDelete(DeleteView):
    model = Data
    success_url = reverse_lazy('author-list')