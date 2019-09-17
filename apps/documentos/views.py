from django.shortcuts import render
from django.views.generic import CreateView
from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['nome', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.proprietario_id = self.kwargs['funcionario_id']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)