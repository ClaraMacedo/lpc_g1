from django.contrib import admin
from evento.models import Evento, EventoCientifico, Pessoa, Autor, PessoaJuridica, PessoaFisica, ArtigoCientifico, TipoDeInscricao, Inscricao


admin.site.register(EventoCientifico)
admin.site.register(Pessoa)
admin.site.register(Autor)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(ArtigoCientifico)
admin.site.register(TipoDeInscricao)
admin.site.register(Inscricao)
admin.site.register(Evento)
