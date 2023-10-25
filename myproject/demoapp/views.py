from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.
def data(request):
    return HttpResponse("this is first app")
def fun(request):
    return render(request,"mini.html")
def data1(request):
    return render(request,"mini2.html",{"name":"Bujji@@@"})
    
def InsertData(request):
    data=Student.objects.all()
    context={"data":data}
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/InsertData")
    return render(request,"index.html",context)

def update(request,id):
    
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        age=request.POST["age"]
        gender=request.POST["gender"]

        edit=Student.objects.get(id=id)
        edit.name=name 
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        return redirect("/InsertData")
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def delete(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/InsertData")
