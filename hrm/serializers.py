from rest_framework_mongoengine import serializers
from hrm.models import Employee, Designation, Department


class EmployeeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DesignationSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class DepartmentSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Department
        fields = '__all__'