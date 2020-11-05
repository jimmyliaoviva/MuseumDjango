from django.shortcuts import render


# Create your views here.
def test(request):
    return render(request, 'testing.html')


def index(request):
    return render(request, 'index.html')
