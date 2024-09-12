from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializer import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):
        try: 
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'company might not exists !!'
            })
            
class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


