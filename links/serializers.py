from .models import Director, SeniorManager, Manager, SeniorDeveloper, JuniorDeveloper

from rest_framework.serializers import ModelSerializer


class JuniorDeveloperSerializer(ModelSerializer):
    class Meta:
        model=JuniorDeveloper
        fields=['id', 'firstName', 'lastName', 'employmentNo']


class SeniorDeveloperSerializer(ModelSerializer):
    juniorDevelopers = JuniorDeveloperSerializer(source='juniordeveloper_set', many=True)

    class Meta:
        model=SeniorDeveloper
        fields = ('id', 'firstName', 'lastName', 'employmentNo', 'juniorDevelopers')


class ManagerSerializer(ModelSerializer):
    seniorDevelopers = SeniorDeveloperSerializer(source='seniordeveloper_set', many=True)

    class Meta:
        model=Manager
        fields = ('id', 'firstName', 'lastName', 'employmentNo', 'seniorDevelopers')


class SeniorManagerSerializer(ModelSerializer):
    managers = ManagerSerializer(source='manager_set', many=True)

    class Meta:
        model=SeniorManager
        fields = ('id', 'firstName', 'lastName', 'employmentNo', 'managers')


class DirectorSerializer(ModelSerializer):
    seniorManagers = SeniorManagerSerializer(source='seniormanager_set', many=True)

    class Meta:
        model=Director
        fields = ('id','firstName', 'lastName', 'employmentNo', 'seniorManagers')

        


