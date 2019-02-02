from django.shortcuts import render

def about_this_site(request):
    return render(request, 'general/about_this_site.html', {})
