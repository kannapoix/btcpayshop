from django.shortcuts import render
from.models import Item

def index(request):
    items = Item.objects.filter(shop = 1)
    return render(request, 'item/index.html', {'items': items})
