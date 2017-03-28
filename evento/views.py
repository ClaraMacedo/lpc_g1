# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Evento, EventoCientifico, Pessoa, Autor, PessoaJuridica, PessoaFisica, ArtigoCientifico, TipoDeInscricao, Inscricao


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                    <li><a href='/eventoCientifico'>Eventos Cientificos</a></li>
                    <li><a href='/pessoa'>Pessoas</a></li>
                    <li><a href='/pessoaFisica'>Pessoas Físicas</a></li>
                    <li><a href='/pessoaJuridica'>Pessoas Juridicas</a></li>
                    <li><a href='/autor'>Autores</a></li>
                    <li><a href='/artigoCientifico'>Artigos Cientificos</a></li>
                </ul>
            """
    return HttpResponse(html)


def eventoInscricao(request, id):
    retorno = "<h1> Inscritos no Evento</h1>"
    evento = Evento.objects.get(pk=id)
    ##evento.inscricao.dataEHora
    retorno += '</br>Inscritos: '+ str(evento.inscricao.dataEHora)+'</br>'
    return HttpResponse(retorno)

def eventoId(request,id):
    retorno = "<h1>Evento</h1>"
    evento = Evento.objects.get(pk=id)
    retorno += '</br>Nome do Envento: {}</br>Evento Principal: {}</br>Data e Hora Inicio: {}</br>Palavras Chave: {}</br>Logotipo: {}</br>Realizador: {}</br>Cidade: {}</br>UF: {}</br>Endereco: {}</br>CEP: {}</br>'.format(evento.nome,evento.eventoPrincipal,evento.dataEHoraDeInicio,evento.palavrasChave,evento.logotipo,str(evento.realizador),evento.cidade,evento.uf,evento.endereco, evento.cep)
    return HttpResponse(retorno)


def listaEvento(request):
    retorno = "<h1>Eventos</h1>"
    lista = Evento.objects.all()
    for evento in lista:
        retorno += '</br>Nome do Envento: {}</br>Evento Principal: {}</br>Data e Hora Inicio: {}</br>Palavras Chave: {}</br>Logotipo: {}</br>Realizador: {}</br>Cidade: {}</br>UF: {}</br>Endereco: {}</br>CEP: {}</br>'.format(evento.nome,evento.eventoPrincipal,evento.dataEHoraDeInicio,evento.palavrasChave,evento.logotipo,str(evento.realizador),evento.cidade,evento.uf,evento.endereco, evento.cep)
    return HttpResponse(retorno)

def eventoCientificoId(request,id):
    retorno = "<h1> Evento Cientico</h1>"
    evento = EventoCientifico.objects.get(pk=id)
    retorno += '</br>Inscritos: {}</br>'.format(evento.issn)
    return HttpResponse(retorno)

def listaEventoCientifico(request):
    retorno = "<h1>Eventos Cientificos</h1>"
    lista = EventoCientifico.objects.all()
    for evento in lista:
        retorno += '</br>Nome do Envento: {}</br></br>'.format(evento.issn)
    return HttpResponse(retorno)

def pessoaId(request,id):
    retorno = "<h1> Pessoa</h1>"
    pessoa = Pessoa.objects.get(pk=id)
    retorno += '</br>Nome: {}</br>'.format(pessoa.nome)
    return HttpResponse(retorno)

def listaPessoa(request):
    retorno = "<h1>Pessoas</h1>"
    lista = Pessoa.objects.all()
    for pessoa in lista:
        retorno += '</br>Nome: {}</br></br>'.format(pessoa.nome)
    return HttpResponse(retorno)

def pessoaFisicaId(request,id):
    retorno = "<h1> Pessoa Fisica</h1>"
    pessoa = PessoaFisica.objects.get(pk=id)
    retorno += '</br>CPF: {}</br>'.format(pessoa.cpf)
    return HttpResponse(retorno)

def listaPessoaFisica(request):
    retorno = "<h1>Pessoas Fisicas</h1>"
    lista = PessoaFisica.objects.all()
    for pessoa in lista:
        retorno += '</br>CPF: {}</br>'.format(pessoa.cpf)
    return HttpResponse(retorno)

def pessoaJuridicaId(request,id):
    retorno = "<h1> Pessoa Juridica</h1>"
    pessoa = PessoaJuridica.objects.get(pk=id)
    retorno += '</br>CNPJ: {}</br>'.format(pessoa.cnpj)
    return HttpResponse(retorno)

def listaPessoaJuridica(request):
    retorno = "<h1>Pessoas Juridicas</h1>"
    lista = PessoaJuridica.objects.all()
    for pessoa in lista:
        retorno += '</br>CNPJ: {}</br>'.format(pessoa.cnpj)
    return HttpResponse(retorno)

def autorId(request,id):
    retorno = "<h1> Autor</h1>"
    autor = Autor.objects.get(pk=id)
    retorno += '</br>Curriculo: {}</br>'.format(autor.curriculo)
    return HttpResponse(retorno)

def listaAutor(request):
    retorno = "<h1>Autores</h1>"
    lista = Autor.objects.all()
    for autor in lista:
        retorno += '</br>Curriculo: {}</br>'.format(autor.curriculo)
    return HttpResponse(retorno)

def artigoCientificoId(request,id):
    retorno = "<h1>Artigo Cientifico</h1>"
    artigo = ArtigoCientifico.objects.get(pk=id)
    retorno += '</br>Curriculo: {}</br>'.format(artigo.titulo)
    return HttpResponse(retorno)

def listaArtigoCientifico(request):
    retorno = "<h1>Artigos Cientificos</h1>"
    lista = ArtigoCientifico.objects.all()
    for artigo in lista:
        retorno += '</br>Curriculo: {}</br>'.format(artigo.titulo)
    return HttpResponse(retorno)
