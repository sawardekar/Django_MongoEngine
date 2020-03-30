from rest_framework_mongoengine import serializers, fields as field
from rest_framework import fields
from hrm.models import Employee, Designation, Department


class DesignationSerializer(serializers.EmbeddedDocumentSerializer):
    name = fields.CharField(required=True)

    class Meta:
        model = Designation
        fields = '__all__'


class EmployeeSerializer(serializers.DocumentSerializer):
    designation = DesignationSerializer(required=False)
    name = fields.CharField(required=True)
    username = fields.CharField(required=False)
    email = fields.EmailField(required=False)
    emp_id = fields.IntegerField(required=False)
    file = field.FileField(required=False)

    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentSerializer(serializers.DocumentSerializer):
    name = fields.CharField(required=True)
    file = field.FileField(required=False)

    class Meta:
        model = Department
        fields = '__all__'

