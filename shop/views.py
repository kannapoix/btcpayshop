from django.shortcuts import render

def item_list(request):
    return render(request, 'shop/item_list.html', {})
