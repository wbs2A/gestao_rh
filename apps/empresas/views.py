from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

@method_decorator(login_required, name='dispatch')
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse("Foi")


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']