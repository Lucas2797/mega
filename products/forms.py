from django import forms
from .models import Tags, Produto, Imagem, Banner, BannerImages, Contact, Estoque
from config.models import Profile
from django.core.exceptions import ValidationError

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tags']

    def clean(self):
        cleaned_data = super().clean()
        cc_tags = cleaned_data.get("tags")
        mod = Tags.objects.filter(tags = cc_tags)
        if mod.exists():
            raise forms.ValidationError('Tags Já Existe')


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(max_length=100)
    preco = forms.DecimalField(max_digits=5, decimal_places=2)


    class Meta:
        model = Produto
        fields = ['nome', 'preco']


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['product', 'quantidade', 'tamanho']



class ImagemForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Imagem
        exclude = ('product', )


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('nome', 'phone', 'email', 'mensagem')

class BannerForm(forms.ModelForm):
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
    nome = forms.CharField(max_length=100)
    tipo = forms.ChoiceField(choices=tipos_banner)

    class Meta:
        model = Banner
        fields = ('nome', 'tipo')


class BannerImagesForm(forms.ModelForm):
    imagem = forms.ImageField(label='banner_image')

    class Meta:
        model = BannerImages
        fields = ('bannering', 'imagem')


class TestForm(forms.Form):
    name = forms.CharField(max_length=100)