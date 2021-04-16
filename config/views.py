from django.shortcuts import render, redirect
from products.models import Produto, Imagem, Tags, Banner, BannerImages, Estoque
from products.forms import ProdutoForm, ImagemForm, TagsForm, BannerForm, BannerImagesForm, ContactForm, EstoqueForm, TestForm
from django.forms import modelformset_factory
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cart.models import Pedido, Item
from config.decorators import allowed_users 
from django.db.models import Q
from cart.models import Item, Pedido
from django.http import HttpResponseRedirect
from django.contrib.auth import logout



                     #BACK#

@allowed_users(allowed_ones=['Admin', 'Vendedor'])
def admin_view(request):
    query = Produto.objects.all()
    context = {
        'query': query,
    }
    if request.user_agent.is_mobile:
        return render(request, 'admin_amp/admin.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'admin/admin.amp.html', context)
    else:
        return render (request, 'admin_amp/admin.amp.html', context)


def login_view(request):
    return render(request, 'desktop/login_test.html')


def register_view(request):
    return render(request, 'admin/signup.amp.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@allowed_users(allowed_ones=['Admin', 'Vendedor'])
def all_products(request):
    query = Produto.objects.all()
    context = {
        'query': query,
    }
    if request.user_agent.is_mobile:
        return render(request, 'admin_amp/all_products.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'admin/all_products.amp.html', context)
    else:
        return render (request, 'admin_amp/all_products.amp.html', context)


@login_required
@allowed_users(allowed_ones=['Admin', 'Vendedor'])
def add_tags(request):
    if request.method == 'POST':
        form = TagsForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = TagsForm()
   
    context = {
        'form': form,
    }
    if request.user_agent.is_mobile:
        return render(request, 'admin_amp/tags_add.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'admin/tags_add.amp.html', context)
    else:
        return render (request, 'admin_amp/tags_add.amp.html', context)


@allowed_users(allowed_ones=['Admin', 'Vendedor'])
def add_product(request):
    if request.method == 'POST':
        prod_form = ProdutoForm(request.POST)
        if prod_form.is_valid():
            prod = prod_form.save(commit=False)
            prod.save()
            print('ok')
            return redirect('update_product', id=prod.id)

    else:
        prod_form = ProdutoForm()

    context = {
        'prod_form': prod_form,
    }
    if request.user_agent.is_mobile:
        return render(request, 'admin_amp/produto_add.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'admin/produto_add.amp.html', context)
    else:
        return render (request, 'admin_amp/produto_add.amp.html', context)

def add_storage(request, id):
    prod = Produto.objects.get(id=id)
    query = Estoque.objects.all()
    if request.method == 'POST':
        storage_form = EstoqueForm(request.POST)
        if storage_form.is_valid():
            storage_form.save()

    else:
        storage_form = EstoqueForm(instance=prod)

    context = {
        'prod': prod,
        'query': query,
        'storage_form': storage_form
    }
    if request.user_agent.is_mobile:
        return render(request, 'admin_amp/storage_add.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'admin/storage_add.amp.html', context)
    else:
        return render (request, 'admin_amp/storage_add.amp.html', context)
    

def company_view(request):
    pass

def suport_view(request):
    pass

@login_required
@allowed_users(allowed_ones=['Admin', 'Vendedor'])
def add_banner(request):
    BannerImageFormSet = modelformset_factory(BannerImages, fields=('imagem',), extra=4)
    if request.method == 'POST':
        form = BannerForm(request.POST)
        form2 = BannerImageFormSet(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            banner = form.save(commit=False)
            banner.save()
            for f in form2:
                try:
                    photo = BannerImages(banner=banner, imagem=f.cleaned_data['imagem'])
                    photo.save()

                except Exception as e:
                    break
            return redirect('/products/admin')
    else:
        form = BannerForm()
        form2 = BannerImageFormSet(queryset=Imagem.objects.none())
    context = {
        'form': form,
        'form2': form2,

    }
    if request.user_agent.is_mobile:
        return render(request, 'admin_amp/banner_add.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'admin/banner_add.amp.html', context)
    else:
        return render (request, 'admin_amp/banner_add.amp.html', context)
    

@allowed_users(allowed_ones=['Admin', 'Vendedor'])
def update_product(request, id):
    prod = Produto.objects.get(id=id)

    prod_form = ProdutoForm(instance=prod)
    img_form = ImagemForm()
    model_form = TagsForm()
    storage_form = EstoqueForm(instance=prod)

    prod_query = Produto.objects.all()
    img_query = Imagem.objects.all()
    model_query = Tags.objects.all()
    storage_query = Estoque.objects.all()

    t1 = 'no'
    t2 = request.POST
    if request.method == 'POST' and 'producting' in request.POST:
        print('PROD')
        prod_form = ProdutoForm(request.POST, instance=prod)
        t1 = 'product'
        t2 = request.POST
        if prod_form.is_valid():
            prod_form.save()

    elif request.method == 'POST' and 'img' in request.POST:
        print('IMG')
        img_form = ImagemForm(request.POST, request.FILES)
        t1 = 'img'
        t2 = request.POST
        if img_form.is_valid():
            img = img_form.save(commit=False)
            img.product = prod
            img.save()

    elif request.method == 'POST' and 'model' in request.POST:
        print('MODEL')
        model_form = TagsForm(request.POST)
        t1 = 'model'
        t2 = request.POST
        if model_form.is_valid():
            model_form.save()

    elif request.method == 'POST' and 'storage' in request.POST:
        print('STORAGE')
        storage_form = EstoqueForm(request.POST)
        t1 = 'storage'
        t2 = request.POST
        if storage_form.is_valid():
            stg = storage_form.save(commit=False)
            stg.product = prod
            stg.save()


    else:
        prod_form = ProdutoForm(instance=prod)
        img_form = ImagemForm()
        model_form = TagsForm()
        storage_form = EstoqueForm(instance=prod)

    context = {
        'prod': prod,
        'prod_query': prod_query,
        'img_query': img_query,
        'storage_query': storage_query,
        'model_query': model_query,
        'prod_form': prod_form,
        'img_form': img_form,
        'model_form': model_form,
        'storage_form': storage_form,
        't1': t1,
        't2': t2,
    }
    if request.user_agent.is_mobile:
        return render(request, 'admin_amp/update_product.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'admin/update_product.amp.html', context)
    else:
        return render (request, 'admin_amp/update_product.amp.html', context)

def update_image(request, id):
    img = Imagem.objects.get(id=id)
    img.image.url = request.GET.get('Image')
    img.save()


@allowed_users(allowed_ones=['Admin'])
def delete_product(request, id):
    prod = Produto.objects.get(id=id)
    prod.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@allowed_users(allowed_ones=['Admin'])
def delete_image(request, id):
    img = Imagem.objects.get(id=id)
    img.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required
def test_view(request):
    var = get_client_ip(request)
    context = {
        'var': var,
    }

    if request.user_agent.is_mobile:
        return render(request, 'admin_amp/Curriculo-mobile.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'admin/Curriculo.html', context)
    else:
        return render (request, 'admin/Curriculo.html', context)



def verify_view(request):
    return render(request, 'desktop/googlec882ad793913a6cc.html')