from rest_framework import serializers
from .models import MalaysiaLoans

class MalaysiaLoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MalaysiaLoans
        fields = ('id','name', 'description')