from django.db import models


class Paciente(models.Model):
    Nome = models.CharField(max_length=100)
    Cpf = models.CharField('CPF', max_length=11)
    Telefone = models.CharField(max_length=20)
    Email = models.EmailField()
    Nascimento = models.DateField()
    Radiação = models.DecimalField(max_digits=9, decimal_places=2)
    

    def __str__(self):
        return self.Nome
