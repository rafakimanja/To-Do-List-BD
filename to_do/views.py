from django.shortcuts import render
from to_do.models import Tarefa
# Create your views here.


def index(request):

    from datetime import datetime

    if request.method == 'POST':

        nome_tarefa = request.POST.get('tarefa')

        tarefa = Tarefa(realizado=False, descricao=nome_tarefa, data=datetime.now())
        tarefa.save()

    tarefas = Tarefa.objects.all()

    return render(request, 'index.html', {'tarefas': tarefas})
