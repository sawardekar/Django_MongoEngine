from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from bson import ObjectId
from django.http import Http404
from hrm.models import Employee
from hrm.serializers import EmployeeSerializer


class EmployeeDetail(APIView):
    parser_class = (FileUploadParser,)

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            employee = self.get_object(pk)
            serializer = EmployeeSerializer(employee)
        else:
            employee = Employee.objects.all()
            serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
