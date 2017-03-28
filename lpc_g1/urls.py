"""lpc_g1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from evento.views import inicio,eventoInscricao, eventoId, listaEvento, listaEventoCientifico,  listaPessoa, listaPessoaFisica, listaPessoaJuridica,   pessoaJuridicaId, pessoaFisicaId,   eventoId, eventoCientificoId, pessoaId, listaAutor, listaArtigoCientifico, autorId, artigoCientificoId

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name='inicio'),
    url(r'^eventosInscritos/(?P<id>[0-9]){1}/', eventoInscricao),
    url(r'^eventos/$', listaEvento, name='listaEvento'),
    url(r'^eventos/(?P<id>[0-9]){1}/', eventoId),
    url(r'^eventoCientifico/$', listaEventoCientifico, name='listaEventoCientifico'),
    url(r'^eventoCientifico/(?P<id>[0-9]){1}/', eventoCientificoId),
    url(r'^pessoa/$', listaPessoa, name='listaPessoa'),
    url(r'^pessoa/(?P<id>[0-9]){1}/', pessoaId),
    url(r'^pessoaFisica/$', listaPessoaFisica, name='listaPessoaFisica'),
    url(r'^pessoaFisica/(?P<id>[0-9]){1}/', pessoaFisicaId),
    url(r'^pessoaJuridica/$', listaPessoaJuridica, name='listaPessoaJuridica'),
    url(r'^pessoaJuridica/(?P<id>[0-9]){1}/', pessoaJuridicaId),
    url(r'^autor/$', listaAutor, name='listaAutor'),
    url(r'^autor/(?P<id>[0-9]){1}/', autorId),
    url(r'^artigoCientifico/$', listaArtigoCientifico, name='listaArtigoCientifico'),
    url(r'^artigoCientifico/(?P<id>[0-9]){1}/', artigoCientificoId),
]
