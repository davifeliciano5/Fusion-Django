from email.policy import default
import uuid
from django.db import models

from stdimage.models import  StdImageField

def git_file_path(_instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação',auto_now_add=True)
    modificado = models.DateField('Atualização',auto_now=True)
    ativo = models.BooleanField('Ativo?',default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni lni-cog','Engrenagem'),
        ('lni lni-stats-up', 'Gráfico'),
        ('lni lni-users', 'Usuários'),
        ('lni lni-layers', 'Design'),
        ('lni lni-mobile', 'Mobile'),
        ('lni lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço',max_length=100)
    descricao = models.CharField('Descrição',max_length=200)
    icone = models.CharField('Icone',max_length=100,choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo',max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome',max_length=100)
    cargo = models.ForeignKey('core.Cargo',verbose_name='Cargo',on_delete=models.CASCADE)
    bio = models.CharField('Bio',max_length=200)
    imagem = StdImageField('Imagem',upload_to=git_file_path,variations={'thumb':{'width':480,'height':480,'crop':True}})
    facebook = models.CharField('Facebook',max_length=100,default='#')
    Instagram = models.CharField('Instagram',max_length=100,default='#')
    twitter = models.CharField('Twitter',max_length=100,default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class ferramenta(Base):
    ICONE_CHOICES = (
        ("lni lni-rocket","Foguete"),
        ("lni lni-laptop-phone", "Celular"),
        ("lni lni-cog", "Engrenagem"),
        ("lni lni-leaf", "folha"),
        ("lni lni-layers", "Camadas"),
        ("lni lni-leaf", "folha2"),
    )
    Ferramenta = models.CharField("Ferramenta",max_length=100)
    Descricao = models.CharField("Descrição",max_length=100)
    iconeFerramenta = models.CharField('Icone',max_length=100,choices=ICONE_CHOICES)
    class Meta:
        verbose_name = 'Ferramenta'
        verbose_name_plural = 'Ferramentas'

    def __str__(self):
        return self.Ferramenta

