from .serializer import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes, api_view


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def SignUp(request):
    try:
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']

        if User.objects.filter(username=username).exists():
            return HttpResponse('This username is already Exists', status=409)

        else:
            user = User(username=username, first_name=first_name,
                        last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            data = UserSerializer(user)
            return Response(data.data, status=status.HTTP_201_CREATED)
    except:
        return Response({'details':'bad request'}, status=status.HTTP_400_BAD_REQUEST)


