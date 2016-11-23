from django.urls import reverse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import Analise, Classe, Data, Table

from django.contrib import messages

class AvaliationNew(CreateView):
    model = Analise
    fields = ['titulo', 'csv', 'csvDel', 'csvQuo']
    template_name = 'core/create.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.saveCsv()
        self.object.calcSturges()
        self.object.catClasses()
        self.object.constructTable()

        messages.add_message(
            self.request, messages.SUCCESS, 'Atividade submetida com sucesso!',
            fail_silently=True,
        )
        return redirect('/view/' + str(self.object.id ))

def index(request):

    return render(request, 'base.html', { })

def view(request, id):
    analise = Analise.objects.get(pk=id)

    bar_graph_x_min = analise.classes.all().order_by('inicio').first().inicio
    bar_graph_x_max = analise.classes.all().order_by('-fim').first().fim
    bar_graph_y_min = analise.tables.all().order_by('fi').first().fi
    bar_graph_y_max = analise.tables.all().order_by('-fi').first().fi

    return render(request, 'core/view.html', {
        'analise': analise,
        'tables': analise.tables.all(),
        'bar_graph_x_min': bar_graph_x_min,
        'bar_graph_x_max': bar_graph_x_max,
        'bar_graph_y_min': bar_graph_y_min,
        'bar_graph_y_max': bar_graph_y_max,
    })
