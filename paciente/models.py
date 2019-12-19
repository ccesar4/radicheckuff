from django.db import models


class Paciente(models.Model):
    Nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    Radiação = models.DecimalField(max_digits=9, decimal_places=2)
    

    def __str__(self):
        return self.Nome
