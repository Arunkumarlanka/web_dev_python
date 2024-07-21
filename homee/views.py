from django.shortcuts import render, HttpResponse
import joblib

model=joblib.load('static/random_forest_regressor')

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def prediction(request):
    if request.method == "POST":
        print("enter into the post request")
        age= request.POST.get('age')
        sex= request.POST.get('sex')
        bmi=request.POST.get('bmi')
        children=request.POST.get('children')
        smoker=request.POST.get('smoker')
        region=request.POST.get('region')
        print(age,bmi,sex,children,smoker,region)
        pred=model.predict([[age,bmi,sex,children,smoker,region]])
        print(pred)
        output={
            "output":pred
        }
        return render(request,'prediction.html',output)
    else:
        return render(request, 'prediction.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')