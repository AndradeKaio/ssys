from rest_framework import viewsets, generics
from rest_framework.response import Response

from api.serializers import EmployeeSerializer
from api.models import Employee

from datetime import date

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeViewAge(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        today_year = date.today().year

        #filter the queryset
        older = queryset.latest('birth_date')
        younger = queryset.earliest('birth_date')
        
        #calculate ages
        older_age = today_year - older.birth_date.year
        younger_age = today_year - younger.birth_date.year
        average = (younger_age + older_age) / 2

        #serialize objects
        younger_s = EmployeeSerializer(younger)
        older_s = EmployeeSerializer(older)

        #add top level info
        data = {'younger': younger_s.data, 'older': older_s.data, 'average': average}
        return Response(data)

class EmployeeViewSalary(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        #filter the queryset
        older = queryset.latest('birth_date')
        younger = queryset.earliest('birth_date')

        average = (older.salary + younger.salary) / 2

        #serialize objects
        younger_s = EmployeeSerializer(younger)
        older_s = EmployeeSerializer(older)

        #add top level info
        data = {'younger': younger_s.data, 'older': older_s.data, 'average': average}
        return Response(data)
