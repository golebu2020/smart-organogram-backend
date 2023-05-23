from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Director, SeniorManager, Manager, SeniorDeveloper, JuniorDeveloper
from .serializers import DirectorSerializer, SeniorManagerSerializer, ManagerSerializer


class OrganogramList(APIView):
    # This gets displays the entire organization architecture
    # http://127.0.0.1:8000/api/organogram/
    def get(self, request, *args, **kwargs):
        organogram = Director.objects.all()
        serializer = DirectorSerializer(organogram, many=True)
        return Response(serializer.data)

    # Saved a Manager under SeniorManager
    # http://127.0.0.1:8000/api/organogram/
    def post(self, request, *args, **kwargs):
        levelName = request.data['levelName']
        levelPosition = request.data['levelPosition']
        firstName = request.data["firstName"]
        lastName = request.data["lastName"]
        employmentNo = request.data["employmentNo"]

        if levelName == "seniorManagers":
            sm = SeniorManager.objects.get(pk=int(levelPosition))
            manager = Manager.objects.create(
                seniorManager=sm, firstName=firstName, lastName=lastName, employmentNo=employmentNo)
            serializer = ManagerSerializer(manager, many=False)
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        levelName = request.data['levelName']
        levelPosition = request.data['levelPosition']
        firstName = request.data['firstName']
        lastName = request.data['lastName']
        isRemove = bool(request.data["isRemove"])

        if levelName == "seniorManagers":
            seniorManager = SeniorManager.objects.get(pk=int(levelPosition))
            if isRemove:
                seniorManager.firstName = ""
                seniorManager.lastName = ""
                seniorManager.employmentNo = ""
            else:
                seniorManager.firstName = firstName
                seniorManager.lastName = lastName
            seniorManager.save()

        elif levelName == "managers":
            manager = Manager.objects.get(pk=int(levelPosition))
            if isRemove:
                manager.firstName = ""
                manager.lastName = ""
                manager.employmentNo = ""
            else:
                manager.firstName = firstName
                manager.lastName = lastName
            manager.save()

        elif levelName == "seniorDevelopers":
            seniorDeveloper = SeniorDeveloper.objects.get(
                pk=int(levelPosition))
            if isRemove:
                seniorDeveloper.firstName = ""
                seniorDeveloper.lastName = ""
                seniorDeveloper.employmentNo = ""
            else:
                seniorDeveloper.firstName = firstName
                seniorDeveloper.lastName = lastName
            seniorDeveloper.save()

        elif levelName == "juniorDevelopers":
            juniorDeveloper = JuniorDeveloper.objects.get(
                pk=int(levelPosition))
            if isRemove:
                juniorDeveloper.firstName = ""
                juniorDeveloper.lastName = ""
                juniorDeveloper.employmentNo = ""
            else:
                juniorDeveloper.firstName = firstName
                juniorDeveloper.lastName = lastName
            juniorDeveloper.save()

        return Response({'message': 'Field updated successfully.'})


class UpdateVacantEmployee(APIView):

    def put(self, request, *args, **kwargs):
        levelName = request.data['levelName']
        levelPosition = request.data['levelPosition']
        firstName = request.data['firstName']
        lastName = request.data['lastName']
        employmentNo = bool(request.data["employmentNo"])
        if levelName == "seniorManagers":
            seniorManager = SeniorManager.objects.get(pk=levelPosition)
            if seniorManager.firstName == "":
                seniorManager.firstName = firstName
                seniorManager.lastName = lastName
                seniorManager.employmentNo = employmentNo
                seniorManager.save()
                return Response({"message": "Successfully added a new employee to the vacant position"})
        elif levelName == "managers":
            manager = Manager.objects.get(pk=levelPosition)
            if manager.firstName == "":
                manager.firstName = firstName
                manager.lastName = lastName
                manager.employmentNo = employmentNo
                manager.save()
                return Response({"message": "Successfully added a new employee to the vacant position"})
        elif levelName == "seniorDevelopers":
            seniorDeveloper = SeniorDeveloper.objects.get(pk=levelPosition)
            if seniorDeveloper.firstName == "":
                seniorDeveloper.firstName = firstName
                seniorDeveloper.lastName = lastName
                seniorDeveloper.employmentNo = employmentNo
                seniorDeveloper.save()
                return Response({"message": "Successfully added a new employee to the vacant position"})
        elif levelName == "juniorDevelopers":
            juniorDeveloper = JuniorDeveloper.objects.get(pk=levelPosition)
            if juniorDeveloper.firstName == "":
                juniorDeveloper.firstName = firstName
                juniorDeveloper.lastName = lastName
                juniorDeveloper.employmentNo = employmentNo
                juniorDeveloper.save()
                return Response({"message": "Successfully added a new employee to the vacant position"})
        return Response({"message": "No Action Recorded"})
