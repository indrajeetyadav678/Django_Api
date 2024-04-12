from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel
from rest_framework.renderers import JSONRenderer
from app.serializers import StudentSerializer


# Create your views here.

def stulist(request):
    stu_list=StudentModel.objects.all()
    print("Query_set =",stu_list )
    serializer=StudentSerializer(stu_list, many=True)
    print("Serializer= ", serializer)
    print("python_data(serializer.data) =", serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print("json_data=", json_data)
    # return render(request, "display.html",json_data )
    return HttpResponse(json_data, content_type='application/json')


def display(request):
    return render(request, "display.html")

def loginform(request):
    if request.method== 'POST':
        Name=request.POST.get('Name')
        Userid=request.POST.get('Userid')
        Number=request.POST.get('Number')
        Password=request.POST.get('Password')
        Con_password=request.POST.get('Con_password')
        label={'Name':Name,'Userid':Userid,'Number':Number,'Password':Password,'Con_password':Con_password}
        StudentModel.objects.create(**label)
        return HttpResponse("DATA Submit sucessfully")
    
def Login(request):
    return render(request, "LoginForm.html")


def stu_detail(request,pk):
    data=StudentModel.objects.get(id=pk)
    print(data)
    serialize=StudentSerializer(data, many=False)
    print(serialize)
    print("Python_data(serializer.data) =",serialize.data)
    json_value=JSONRenderer().render(serialize.data)
    return HttpResponse(json_value, content_type='application/json')

# def deletedata(request):
    