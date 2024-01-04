from django.shortcuts import render
from to_do.models import Tarefa
from datetime import datetime


def index(request):

    tarefas = Tarefa.objects.all()
    flag = False

    if request.method == 'POST':

        nome_tarefa = request.POST.get('tarefa')

        for tf in tarefas:

            if tf.descricao == nome_tarefa:
                print(f'{tf.descricao} ja cadastrado no banco de dados')
                flag = True

        if not flag:
            tarefa = Tarefa(realizado=False, descricao=nome_tarefa, data=datetime.now())
            tarefa.save()

    return render(request, 'index.html', {'tarefas': tarefas})
