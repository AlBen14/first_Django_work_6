from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisment
from .forms import AdvertsForm
from django.core.exceptions import ValidationError
# from django.http import HttpResponse

# Create your views here.

def index(request):
    adverts=Advertisment.objects.all()
    context={"advert":adverts}
    return render(request, 'index.html', context)

def topSellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method=="POST":
        form = AdvertsForm(request.POST ,request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if title[0] == "?":
                raise ValidationError('Нельзя добавить логин со знаком вопроса')
            advertisment = Advertisment(**form.cleaned_data)
            advertisment.user = request.user
            advertisment.save()
            url = reverse('main_page')
        return redirect(url)
    else:
        form = AdvertsForm()
        context = {"form" : form}
        return render(request, 'advertisement-post.html',context)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

