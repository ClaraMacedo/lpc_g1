# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Evento(models.Model):
    nome = models.CharField('nome', max_length=200,   null=True)
    eventoPrincipal =models.CharField('eventoPrincipal', max_length=200,   null=True)
    sigla =models.CharField('sigla', max_length=200,   null=True)
    dataEHoraDeInicio = models.DateField('dataEHoraDeInicio',   null=True)
    palavrasChave =models.CharField('palavrasChave', max_length=200,   null=True)
    logotipo =models.CharField('logotipo', max_length=200,   null=True)
    realizador=models.ForeignKey('Pessoa',   null=True)
    cidade =models.CharField('cidade', max_length=200,null=True)
    uf =models.CharField('uf', max_length=200,   null=True)
    endereco =models.CharField('endereco', max_length=200,   null=True)
    cep =models.CharField('cep', max_length=200,  null=True)
    inscricao = models.ForeignKey('Inscricao',   null=True)

    def save(self):
        self.nome = self.nome.upper()

        super(Evento, self).save()

    def __str__(self):
        return '{}'.format(self.nome)

class EventoCientifico(Evento):
    issn =models.CharField('issn', max_length=200)

    def save(self):
        self.issn = self.issn.upper()
        super(EventoCientifico, self).save()

    def __str__(self):
        return '{}'.format(self.issn)

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email =models.CharField('email', max_length=200)

    def save(self):
        self.nome = self.nome.upper()
        super(Pessoa, self).save()

    def __str__(self):
        return '{}'.format(self.nome)

class Autor(Pessoa):
    curriculo= models.CharField('curriculo', max_length=200)
    artigos=  models.ForeignKey('ArtigoCientifico')

class PessoaJuridica(Pessoa):
    cnpj= models.CharField('cnpj', max_length=200)
    razaoSocial=  models.CharField('razaoSocial', max_length=200)

class PessoaFisica(Pessoa):
    cpf= models.CharField('cpf', max_length=200)

class ArtigoCientifico(models.Model):
    titulo= models.CharField('titulo', max_length=100)
    autores= models.ForeignKey('Autor')
    evento = models.ForeignKey('EventoCientifico')

class TipoDeInscricao(models.Model):
    descricao= models.CharField('descricao', max_length=100)

class Inscricao(models.Model):
    participante= models.ForeignKey('PessoaFisica')
    dataEHora = models.DateField('dataEHora')
    tipoDeInscricao= models.ForeignKey('TipoDeInscricao')
    ##eventoId= models.ForeignKey('Evento')
