from django.shortcuts import render, redirect
from .models import Yeguliklar, Category
from .forms import AloqaForm, Stol_BuyurtmaForm
# Create your views here.
def index(request):
    category = request.GET.get('category')
    if category== None:
        yegulik = Yeguliklar.objects.all()
    else:
        yegulik = Yeguliklar.objects.filter(category__name=category)

    categories = Category.objects.all()

    form = AloqaForm()
    if request.method == 'POST':
        form = AloqaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    buyurtma = Stol_BuyurtmaForm()
    if request.method == 'POST':
        buyurtma = Stol_BuyurtmaForm(request.POST)
        if buyurtma.is_valid():
            buyurtma.save()
            return redirect('/')



    context = {'categories':categories, 'yegulik':yegulik, 'form':form, 'buyurtma':buyurtma}

    return render(request, 'index.html', context)
