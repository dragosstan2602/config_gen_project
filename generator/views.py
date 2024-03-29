from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'generator/home.html')


@csrf_exempt
def index(request):
    if request.method == 'POST':
        # getting values from post
        vendor = request.POST.get('vendor')
        model = request.POST.get('model')

        # adding the values in a context variable
        context_platform = {
            'vendor': vendor,
            'model': model
        }

        return render(request, 'generator/showdata.html', context_platform)
    else:
        return render(request, 'generator/index.html')


def viptela(request):
    return render(request, 'generator/viptela.html')


def adva(request):
    return render(request, 'generator/adva.html')


def cisco_legacy(request):
    return render(request, 'generator/placeholder.html')


def placeholder(request):
    return render(request, 'generator/placeholder.html')


def about(request):
    return render(request, 'generator/about.html')
