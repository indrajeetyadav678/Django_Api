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
    return HttpResponse(json_data, content_type='application/json')

# def stu_detail(request,pk):
#     data=pk
#     return HttpResponse(data)