from rest_framework_mongoengine import viewsets
from hrm.serializers import DepartmentSerializer
from hrm.models import Department
from django.http import HttpResponse


def index(request):
    return HttpResponse('Success')


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Designation to be viewed or edited.
    """
    lookup_field = 'id'
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Department.objects.all()

    def pre_save(self, obj):
        obj.file = self.request.FILES.get('file')




