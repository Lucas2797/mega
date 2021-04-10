from django.contrib import admin
from .models import Produto, Imagem, Tags, Contact, Banner, BannerImages, Contact, Estoque, SubTags



class TagsAdmin(admin.ModelAdmin):
    list_display = ('tags',)
    
class SubTagsAdmin(admin.ModelAdmin):
    list_display = ('tag', 'subtag')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'id', 'updated_time')

class ImagensAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'id')

class BannerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')

class BannerImagesAdmin(admin.ModelAdmin):
    list_display = ('bannering', 'imagem')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'phone', 'email', 'mensagem')

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('product', 'tamanho', 'quantidade')


admin.site.register(Tags, TagsAdmin),
admin.site.register(SubTags, SubTagsAdmin),
admin.site.register(Produto, ProdutoAdmin),
admin.site.register(Imagem, ImagensAdmin),
admin.site.register(Banner, BannerAdmin),
admin.site.register(BannerImages, BannerImagesAdmin),
admin.site.register(Contact, ContactAdmin),
admin.site.register(Estoque, EstoqueAdmin)