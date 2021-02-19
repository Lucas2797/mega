from django.db import models
from django.template.defaultfilters import slugify
from .managers import ProdutoManager, EstoqueManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils import timezone


class Produto (models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)

    objects = ProdutoManager()

    def __str__(self):
        return '%s - %s' % (self.nome, self.preco)
    
    def get_storage_total(self):
        total = 0
        e1 = self.storage.all()
        for e in e1:
            total += e.quantidade
        return total


    def all_buyed(self):
        total = 0
        for e in self.storage.all():
            total += e.quantidade
        for i in self.product_items.filter(is_ordered=True):
            total += i.quantity
        return total

    def all_selled(self):
        total = 0
        for i in self.product_items.filter(is_ordered=True):
            total += i.quantity
        return total

    def sell_percent(self):
        try:
            total = (self.all_selled() * 100)/ self.all_buyed()
            return total
        except ZeroDivisionError:
            return 'sem Vendidos'





class Tags(models.Model):

    tags_choices = [
        ('Eletronico', (
                ('Computador', 'Computador'),
                ('Casa', 'Casa'),
                ('Som', 'Som'),
                ('Video', 'Video'),
                ('Perifericos', 'Perifericos'),
            )
        ),
        ('Acessorio', (
                ('Relogio', 'Relogio'),
                ('Oculos', 'Oculos'),
                ('Joia', 'Joia'),
            )
        ),
        ('Telefone', (
                ('Samsumg', 'Samsumg'),
                ('Xiaomi', 'Xiaomi'),
                ('Huawei', 'Huawei'),
                ('iPhone', 'iPhone'),
                ('Carregador', 'Carregador'),
                ('Fone', 'Fone'),
            )
        ),
        ('unknown', 'Unknown'),
    ]

    product = models.ForeignKey(Produto, related_name='tags', on_delete=models.SET_NULL, null=True)
    tags = models.CharField(max_length=30)

    def __str__(self):
            return '%s-%s-%s' % (self.tags, self.sexo)

    def clean(self):
        mod = Tags.objects.filter(tags = self.tags, publico=self.publico, sexo=self.sexo)
        if mod.exists():
            raise ValidationError('Tags Já Existe')





class Estoque(models.Model):
    product = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, related_name='storage')
    tamanho = models.CharField(max_length=100, null=True)
    quantidade = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    objects = EstoqueManager()


    def __str__(self):
        return '%s - %s - %s' % (self.product,self.tamanho, self.quantidade)

    def clean(self):
        stor = Estoque.objects.filter(product=self.product, tamanho=self.tamanho)
        if stor.exists():
            raise ValidationError('Estoque já existente')
        
        

def get_image_filename(instance, filename):
    nome = instance.product.nome
    slug = slugify(nome)
    return "produto_imagens/%s-%s" % (slug, filename)


class Imagem (models.Model):
    product = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_filename)


class Contact (models.Model):
    nome = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField()
    mensagem = models.TextField(max_length=600, default='Mensagem')

class Banner(models.Model):
    Inicial = 'Inicial'
    Mini = 'Mini'
    Adjacentes = 'Adjacentes'
    Promocao = 'Promocao'
    tipos_banner = [
        (Inicial, 'Inicial'),
        (Mini, 'Mini'),
        (Promocao, 'Promocao'),
        (Adjacentes, 'Adjacentes'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=tipos_banner)

    def __str__(self):
        return '%s %s' % (self.nome, self.tipo)


def get_banner_image_filename(instance, filename):
    nome = instance.bannering.nome
    slug = slugify(nome)
    return "banner_imagens/%s-%s" % (slug, filename)

class BannerImages(models.Model):
    bannering = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='banner_image')
    imagem = models.ImageField(upload_to=get_banner_image_filename)
    link = models.URLField(max_length=200, default='products/home')

    def __str__(self):
        return '%s %s' % (self.bannering, self.imagem)