from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from webapi.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
	# API endpoint that allows user to be viewed/edited
	queryset = User.objects.all().order_by("-date_joined")
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
	# API endpoint for groups
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]