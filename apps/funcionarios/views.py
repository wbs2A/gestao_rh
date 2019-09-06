from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Funcionario
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionario')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    def form_valid(self, form):
        funcionario_obj = form.save(commit=False)
        funcionario_obj.empresa = self.request.user.funcionario.empresa
        _username = funcionario_obj.nome.split(' ')[0] +funcionario_obj.nome.split(' ')[1]
        funcionario_obj.user = User.objects.create(username=_username)
        funcionario_obj.save()
        return super(FuncionarioCreate, self).form_valid(form)

