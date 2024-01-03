#admin.py

from django.contrib import admin

from to_do.models import Tarefa


class ListandoTarefas(admin.ModelAdmin):
    list_display = ('realizado', 'descricao')
    list_display_links = ('realizado', 'descricao')


admin.site.register(Tarefa, ListandoTarefas)
