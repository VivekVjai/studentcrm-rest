from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView

from crm.models import Student

from crm.serializers import StudentSerializer

from rest_framework.response import Response

# Create your views here.
class StudentLiscreatetView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Student.objects.all() #data-baseil ninnu ella datyum edukkan ulla orm query
        #ithu oru query set aanu
        #ithinae native python native type lotu mattanom 
        #athinu use cheyunna aanu serializer 

        serializer_instance=StudentSerializer(qs,many=True)#(serialization)

        return Response(data=serializer_instance.data)

    def post(self,request,*args,**kwargs):

        serializer_instance=StudentSerializer(data=request.data)#initialise cheythu

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
class StudentRetrieveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=get_object_or_404(Student,id=id)

        serializer_instance=StudentSerializer(qs)

        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        student_instance=get_object_or_404(Student,id=id)

        student_instance.delete()

        return Response(data={"message":"deleted"})
    

  