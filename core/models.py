from django.db import models
import math
import csv
from pprint import pprint

# Create your models here.

class Analise(models.Model):
    titulo = models.CharField(max_length=50)
    data_criado = models.DateField(auto_now=True)
    csv = models.FileField(upload_to='uploads/csv')
    csvDel = models.CharField(max_length=1)
    csvQuo = models.CharField(max_length=1)
    numClasses = models.IntegerField(blank=True, null=True)
    variation = models.FloatField(blank=True, null=True)
    media = models.FloatField(blank=True, null=True)
    moda = models.FloatField(blank=True, null=True)
    mediana = models.FloatField(blank=True, null=True)

    def saveCsv(self):
        with open (self.csv.path, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=self.csvDel, quotechar=self.csvQuo)
            for row in spamreader:
                for element in row:
                    data = Data(analise=self, value=float(element), classe=None)
                    data.save()

    def calcSturges(self):
        numClasses = 1 + (3.3 * math.log(self.data.count(), 10))

        numClasses = round(numClasses)
        self.numClasses = numClasses

        variation = (self.data.all().aggregate(models.Max('value'))['value__max'] - self.data.all().aggregate(models.Min('value'))['value__min']) / numClasses
        variation = round(variation)
        self.variation = variation

        self.save()

        classeIni = self.data.all().aggregate(models.Min('value'))['value__min']
        for i in range(0, numClasses):
            classeFim = classeIni + variation
            classe = Classe(analise=self, inicio=classeIni, fim=classeFim )
            classe.save()
            classeIni = classeFim

    def catClasses(self):
        for classe in self.classes.all():
            elements = self.data.filter(value__gte=classe.inicio).filter(value__lt=classe.fim).update(classe=classe)

    def constructTable(self):
        ultimaClasse = None
        ultimaTable = None
        for classe in self.classes.all():
            ultimoFia = ultimaTable.fia if ultimaTable else 0
            table = Table(
                analise=self,
                classe=classe,
                fi=classe.caData.count(),
                fia=classe.caData.count() + ultimoFia,
                fri=round(classe.caData.count() / classe.analise.data.all().count(), 3),
                fria=round((classe.caData.count() + ultimoFia) / classe.analise.data.all().count(), 3),
                xi= (classe.fim + classe.inicio) / 2,
                perc=round((classe.caData.count() / classe.analise.data.all().count())  * 100, 3),
                ang=round(((classe.caData.count() + ultimoFia) / classe.analise.data.all().count()) * 360, 3),
                xifi=1
            )
            table.save()
            ultimaClasse = classe
            ultimaTable = table

    def __str__(self):
        return self.titulo

class Classe(models.Model):
    analise = models.ForeignKey(Analise, related_name="classes")
    inicio = models.FloatField()
    fim = models.FloatField()

    def __str__(self):
        return str(self.inicio) + ' |- ' + str(self.fim)

class Data(models.Model):
    analise = models.ForeignKey(Analise, related_name="data")
    value = models.FloatField()
    classe = models.ForeignKey(Classe, blank=True, null=True, related_name='caData')

class Table(models.Model):
    analise = models.ForeignKey(Analise, related_name="tables")
    classe = models.ForeignKey(Classe, related_name="taClasses")
    fi = models.FloatField()
    fia = models.FloatField()
    fri = models.FloatField()
    fria = models.FloatField()
    xi = models.FloatField()
    perc = models.FloatField()
    ang = models.FloatField()
    xifi = models.FloatField()
