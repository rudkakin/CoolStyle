from django.shortcuts import render
from django.http import HttpResponse
from .models import Clothes
from .forms import ClothesForm
import csv

# Create your views here.
def index(request):
    return render(request, 'main/shopmenu.html')


def bucket(request):
    clothes = Clothes.objects.all()
    return render(request, 'main/basket.html', {'clothes': clothes})


def create(request):
    form = ClothesForm()
    context = {
        'form': form
    }
    return render(request, 'main/object.html', context)


def mens(request):
    mens = []
    womens = []
    children = []
    with open('C:\\Users\\aidar\\Desktop\\Python\\coolstyle\\main\\clothes.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            listing = ''.join(row).split(';')
            wear = Clothes()
            wear.sex = listing[0]
            wear.category = listing[1]
            wear.title = listing[2]
            wear.composition = listing[3]
            wear.size = listing[4]
            wear.price = listing[5]
            wear.image = listing[6]
            if listing[0] == 'Мужской':
                mens.append(wear)
            elif listing[0] == 'Женский':
                womens.append(wear)
            else:
                children.append(wear)
    return render(request, 'main/mens.html', {'mens': mens, 'womens': womens, 'children': children})


def womens(request):
    mens = []
    womens = []
    children = []
    with open('C:\\Users\\aidar\\Desktop\\Python\\coolstyle\\main\\clothes.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            listing = ''.join(row).split(';')
            wear = Clothes()
            wear.sex = listing[0]
            wear.category = listing[1]
            wear.title = listing[2]
            wear.composition = listing[3]
            wear.size = listing[4]
            wear.price = listing[5]
            wear.image = listing[6]
            if listing[0] == 'Мужской':
                mens.append(wear)
            elif listing[0] == 'Женский':
                womens.append(wear)
            else:
                children.append(wear)
    return render(request, 'main/womens.html', {'mens': mens, 'womens': womens, 'children': children})


def kids(request):
    mens = []
    womens = []
    children = []
    with open('C:\\Users\\aidar\\Desktop\\Python\\coolstyle\\main\\clothes.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            listing = ''.join(row).split(';')
            wear = Clothes()
            wear.sex = listing[0]
            wear.category = listing[1]
            wear.title = listing[2]
            wear.composition = listing[3]
            wear.size = listing[4]
            wear.price = listing[5]
            wear.image = listing[6]
            if listing[0] == 'Мужской':
                mens.append(wear)
            elif listing[0] == 'Женский':
                womens.append(wear)
            else:
                children.append(wear)
    return render(request, 'main/kids.html', {'mens': mens, 'womens': womens, 'children': children})