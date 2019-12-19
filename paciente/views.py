from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm


def list_paciente(request):
    paciente = Paciente.objects.all()
    return render(request, 'paciente.html', {'paciente': paciente})


def create_paciente(request):
    form = PacienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_paciente')

    return render(request, 'paciente-form.html', {'form': form})


def update_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    form = PacienteForm(request.POST or None, instance=paciente)

    if form.is_valid():
        form.save()
        return redirect('list_paciente')

    return render(request, 'paciente-form.html', {'form': form, 'paciente': paciente})


def delete_paciente(request, id):
    paciente = Paciente.objects.get(id=id)

    if request.method == 'POST':
        paciente.delete()
        return redirect('list_paciente')

    return render(request, 'paciente-delete-confirm.html', {'paciente': paciente})
