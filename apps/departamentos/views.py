from django.shortcuts import render
from django.views.generic import ListView
from .models import Departamento
# Create your views here.
class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        _empresa = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=_empresa)