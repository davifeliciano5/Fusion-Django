from django.contrib import admin

from .models import Cargo,Servico,Funcionario,ferramenta

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo','ativo','modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','icone','ativo','modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo','modificado','ativo')

@admin.register(ferramenta)
class ferramentaAdmin(admin.ModelAdmin):
    list_display = ('Ferramenta','Descricao','iconeFerramenta','ativo')
