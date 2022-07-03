from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from math import floor, ceil

FOR_OVERWEIGHT = 24.9
FOR_UNDERWEIGHT = 18.5


def index(request):
    return render(request, 'bmi/index.html')


def find(request):

    weight = request.POST['weight']
    height = request.POST['height']
    if(weight):
        weight = float(weight)
    if(height):
        height = float(height)

    bmi = 100.00
    text = ""
    healthy_weight = 0
    error = False

    try:
        bmi = weight/(height**2)
        if (bmi >= 24.9):
            healthy_weight = floor(FOR_OVERWEIGHT * (height**2))
        else:
            healthy_weight = ceil(FOR_UNDERWEIGHT * (height**2))

        if (bmi < 18.5):
            text = "Underweight"
        elif (bmi >= 18.5 and bmi <= 24.9):
            text = "Healthy"
        elif (bmi >= 25 and bmi < 30):
            text = "Overweight"
        elif (bmi >= 30 and bmi < 35):
            text = "Obese"
        else:
            text = "ExtremelyObese"

    except Exception as e:  # work on python 3.x
        print('*****ERROR: ' + str(e))
        print("*****ERROR: CALCULATION ERROR CHECK HEIGHT****")
        error = True
        text = "Coudnt Find Your BMI Pleas Enter Proper Height Input"

    context = {
        'bmi': round(bmi, 2),
        'category': text,
        'healthy_weight': healthy_weight,
        'error': error
    }

    return render(request, 'bmi/result.html', context)
