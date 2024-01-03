from django.shortcuts import render


def front_page(request):
    return render(request, 'core/frontpage.html')


def about_us(request):
    return render(request, 'core/about.html')