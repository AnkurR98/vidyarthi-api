from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from account.models import Account
from me.models import CollaborateModel, ProjectModel, CourseModel
from me.api.serializers import CollaborateSerializer, ProjectSerializer, CourseSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def collaborate_read_view(request):
    try:
        collaborate = CollaborateModel.objects.get(
            userId=request.query_params.get('userId'))
    except CollaborateModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollaborateSerializer(collaborate)
        return Response(serializer.data)


# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def collaborate_create_view(request):

    if request.method == 'POST':

        data = request.data
        data['author'] = request.user.pk
        serializer = CollaborateSerializer(data=data)

        data = {}
        if serializer.is_valid():
            collaborate_detail = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['userId'] = collaborate_detail.userId
            data['workDuring'] = collaborate_detail.workDuring
            data['otherWorkDuring'] = collaborate_detail.otherWorkDuring
            data['workWith'] = collaborate_detail.workWith
            data['communicateOver'] = collaborate_detail.communicateOver
            data['communicateWith'] = collaborate_detail.communicateWith
            data['workBy'] = collaborate_detail.workBy
            data['otherWorkBy'] = collaborate_detail.otherWorkBy
            data['workHours'] = collaborate_detail.workHours
            data['otherWorkHours'] = collaborate_detail.otherWorkHours
            data['projectDuration'] = collaborate_detail.projectDuration

            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def project_read_view(request):
    try:
        project = ProjectModel.objects.get(
            userId=request.query_params.get('userId'))
    except ProjectModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def project_create_view(request):

    if request.method == 'POST':

        data = request.data
        data['author'] = request.user.pk
        serializer = ProjectSerializer(data=data)

        data = {}
        if serializer.is_valid():
            project_detail = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['projectTitle'] = project_detail.projectTitle
            data['projectLink'] = project_detail.projectLink
            data['about'] = project_detail.about
            data['primaryTrack'] = project_detail.primaryTrack
            data['userId'] = project_detail.userId

            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def course_read_view(request):
    try:
        course = CourseModel.objects.get(
            userId=request.query_params.get('userId'))
    except CourseModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def course_create_view(request):

    if request.method == 'POST':

        data = request.data
        data['author'] = request.user.pk
        serializer = CourseSerializer(data=data)

        data = {}
        if serializer.is_valid():
            course_detail = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['courseTitle'] = course_detail.courseTitle
            data['courseLink'] = course_detail.courseLink
            data['coursePublisher'] = course_detail.coursePublisher
            data['primaryTrack'] = course_detail.primaryTrack
            data['rating'] = course_detail.rating
            data['difficulty'] = course_detail.difficulty
            data['userId'] = course_detail.userId

            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
