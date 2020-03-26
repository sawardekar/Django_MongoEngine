from django.conf.urls import url,include
from rest_framework import routers
from hrm import views
from hrm.apiviews import EmployeeDetail

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet, basename="Department")

urlpatterns = [
    url('', include(router.urls)),
    url(r'^index', views.index),
    url(r'^emp/$', EmployeeDetail.as_view()),
    url(r'^emp/(?P<pk>[a-z0-9]+)/$', EmployeeDetail.as_view()),
]