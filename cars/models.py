from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100, verbose_name='Modelo')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Marca')
    factory_year = models.IntegerField(null=True, verbose_name='Ano de fabricação')
    model_year = models.IntegerField(null=True, verbose_name='Ano do modelo')
    color = models.CharField(max_length=50, null=True, blank=True, verbose_name='Cor')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True,
                              verbose_name='Proprietário')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['model']
        verbose_name = 'Carro'

    def __str__(self):
        return self.model
