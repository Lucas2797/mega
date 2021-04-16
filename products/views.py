from django.shortcuts import render, redirect
from .models import Produto, Imagem, Tags, Banner, BannerImages, Estoque
from django.urls import reverse
from django.shortcuts import get_object_or_404
from cart.models import Pedido, Item
from django.db.models import Q
from cart.models import Item, Pedido
from django.utils import timezone
from .forms import ContactForm


#FRONT#
def home_view(request):
    if Banner.objects.filter(tipo='Inicial'):
        for b in Banner.objects.filter(tipo='Inicial'):
            filter1 = b.banner_image.all()
    else:
        filter1 = None
    filter2 = Banner.objects.filter(tipo='Mini')
    filter3 = Produto.objects.filter(storage__updated_time__gte=timezone.now() - timezone.timedelta(days=15))
    context = {
        'filter1': filter1,
        'filter2': filter2,
        'filter3': filter3,
        }
    if request.user_agent.is_mobile:
        return render(request, 'amp/home.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/home.amp.html', context)
    else:
        return render (request, 'amp/home.amp.html', context)
    
    

def get(request):
    return self.object


def list_view1(request, tag):
    query = Produto.objects.filter(tag__tags=tag)
    context = {
        'query': query,
    }
    return render(request, 'desktop/AllList.amp.html', context)



def list_view(request):
    model_query = request.GET.get('model_query', '')
    price_query = request.GET.get('price_query', '')
    size_query_all = request.GET.get('size_query_all', '')
    size_query_calsa = request.GET.get('size_query_calsa', '')
    sex_query = request.GET.get('sex_query', '')

    if model_query or price_query or size_query_all:
        if model_query == 'CALSA':
            query = Produto.objects.filter(Q(model__tags__icontains='CALSA'),
                Q(preco__lte=price_query),
                Q(storage__tamanho__gte=size_query_calsa),
                Q(model__sexo__icontains=sex_query),
                Q(storage__quantidade__gt=0)).distinct

        else:
            query = Produto.objects.filter(Q(model__tags__icontains=model_query),
                Q(preco__lte=price_query),
                Q(storage__tamanho__gte=size_query_all),
                Q(model__sexo__icontains=sex_query),
                Q(storage__quantidade__gt=0)).distinct
    
    
    else:
        query = Produto.objects.filter(storage__quantidade__gt=0).distinct()

        context = {
            'query': query
        }
    if request.user_agent.is_mobile:
        return render(request, 'amp/AllList.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/AllList.amp.html', context)
    else:
        return render (request, 'amp/AllList.amp.html', context)

def detail_view(request, id):
    prod = get_object_or_404(Produto, pk=id)
    query = Produto.objects.filter(model=prod.model)
    context = {
        'prod': prod,
        'query': query,
    }
    if request.user_agent.is_mobile:
        return render(request, 'amp/detail.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/detail.amp.html', context)
    else:
        return render (request, 'desktop/detail.amp.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_product')

    else:
        form = ContactForm()


    context = {'form': form}
    if request.user_agent.is_mobile:
        return render(request, 'amp/contact.amp.html', context)
    elif request.user_agent.is_pc:
        return render (request, 'desktop/contact.amp.html', context)
    else:
        return render (request, 'desktop/contact.amp.html', context)


def chat_view(request):
    if request.user_agent.is_mobile:
        return render(request, 'amp/chat.amp.html')
    elif request.user_agent.is_pc:
        return render (request, 'desktop/chat.amp.html')
    else:
        return render (request, 'desktop/chat.amp.html')



def company_view(request):
    pass

def suport_view(request):
    pass

def search_view(request):
    search_query = request.GET.get('search_query', '')
    filter1 = Produto.objects.filter(nome__unaccent__lower__trigram_similar=search_query)

    context = {
        'search_query': search_query,
        'filter1': filter1,
    }
    
    return render (request, 'desktop/search.amp.html', context)


def test_amp_view(request):
    context = {
        
    }
    return render(request, 'admin/test.amp.html', context)


def test_view(request):
    context = {
        
    }
    return render(request, 'admin/test.html', context)

