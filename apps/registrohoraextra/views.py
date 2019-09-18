from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import RegistroHoraExtra
class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo_hora_extra    ', 'funcionario', 'horas']