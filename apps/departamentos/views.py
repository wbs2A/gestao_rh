from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento
# Create your views here.
class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        _empresa = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=_empresa)

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate,self).form_valid(form)

class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')