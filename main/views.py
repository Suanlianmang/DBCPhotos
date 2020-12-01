from django.shortcuts import render
from .models import image
from django.views.generic import CreateView

def home(request):
    images = three(image.objects.order_by('-time')[:1000])
    contex = {
        'images1' : images[0],
        'images2' : images[1],
        'images3' : images[2],
        }
    return render(request, 'main/index.html', contex)
def catagory(request, name):
    images = three(image.objects.filter(title = name))
    page = name
    contex = {
        'cat1' : images[0],
        'cat2' : images[1],
        'cat3' : images[2],
        'page' : page,
        }
    return render(request, 'main/catagory.html', contex)
class UploadView(CreateView):
    model = image
    fields = ['title', 'img']


def three(index):
    obj = index
    obj1 = []
    obj2 = []
    obj3 = []
    for i in range(len(obj)):
        if i % 3 == 0:
            obj1.append(obj[i])
        if i % 3 == 1:
            obj2.append(obj[i])
        if i % 3 == 2:
            obj3.append(obj[i])
    return obj1, obj2, obj3
            