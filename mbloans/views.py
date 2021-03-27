from rest_framework import viewsets
from  .serializers import MalaysiaLoanSerializer
from .models import MalaysiaLoans

# Create your views here.
class MalaysiaLoanViewSet(viewsets.ModelViewSet):
    queryset =MalaysiaLoans.objects.all().order_by('name')
    serializer_class =MalaysiaLoans