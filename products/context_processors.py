from .models import Tags


def add_tags_base(request):
    tags = Tags.objects.all()
    return { 'tags': tags }



