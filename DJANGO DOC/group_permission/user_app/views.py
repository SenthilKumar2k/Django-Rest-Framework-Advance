from django.contrib.auth.models import User,Group, Permission
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from .models import News_letter
from .permissions import CanPublishNewsletter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Group_View(APIView):
    def post(self, request):
        data=request.data
        group=Group.objects.create(name=data['role'])
        return Response({"message":"success"}, status=status.HTTP_200_OK)
    
    def get(self, request, pk=None):
        group_list=Group.objects.all()
        response=[]
        for group in group_list:
            response.append(group.name)
        return Response(response, status=status.HTTP_200_OK)
    
class User_Create(APIView):
    def post(self, request):
        data=request.data
        user=User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
        return Response({'message':'success'}, status=status.HTTP_200_OK)
    
    def get(self, request, pk=None):
        user_list=User.objects.all()
        response=[]
        for user in user_list:
            response.append(user.username)
        return Response(response, status=status.HTTP_200_OK)
    
class Permission_view(APIView):

    def post(self, request):
        content_type=ContentType.objects.get_for_model(News_letter)
        Permission.objects.create(
            codename="create_newsletter",
            name= "can create a newsletter",
            content_type= content_type
        )
        return Response({'message':'Permission created'}, status=status.HTTP_200_OK)

    def get(self, request):
        permission=Permission.objects.all()
        response=[{"id":perm.id,
                   "codename":perm.codename,
                   "name":perm.name,
                   "app_label":perm.content_type.app_label,
                   "model":perm.content_type.model}
                  for perm in permission]
        return Response(response, status=status.HTTP_200_OK)
# [
# {"id": 39, "codename": "edit_newsletter", "name": "can edit an newsletter", "app_label": "user_app",
#         "model": "news_letter"},
# {"id": 37, "codename": "publish_newsletter", "name": "can publish an newsletter", "app_label": "user_app",
#         "model": "news_letter"},
# {"id": 40, "codename": "review_newsletter", "name": "can review an newsletter", "app_label": "user_app",
#         "model": "news_letter"},
# {"id": 38, "codename": "unpublish_newsletter", "name": "can unpublish an newsletter", "app_label": "user_app",
#         "model": "news_letter"},
# {"id": 42, "codename": "create_newsletter", "name": "can create a newsletter", "app_label": "user_app",
#         "model": "news_letter"},
# {"id": 41, "codename": "share_newsletter", "name": "can share a newsletter", "app_label": "user_app",
#         "model": "news_letter"}
# ]

    def delete(self, request):
        permission=Permission.objects.filter(id__in=[25,26,27,28,31,29,30,32,33,34,35,36]).delete()
        return Response({"message":"success"}, status=status.HTTP_200_OK)
    
class Group_Permission_View(APIView):
    def post(self, request):
        group=Group.objects.get(name="publisher")
        list_permission=[ "unpublish_newsletter", "review_newsletter", "publish_newsletter"]
        for i in list_permission:
            permission=Permission.objects.get(codename=i)
            group.permissions.add(permission)
        return Response({"message":"success"}, status=status.HTTP_200_OK)
        
class User_Group_Add_View(APIView):
    def post(self, request):
        user=User.objects.get(username='kiran')
        group=Group.objects.get(name='publisher')
        user.groups.add(group)
        return Response({"message":"User is added to the group"}, status=status.HTTP_200_OK)

class User_Permission_view(APIView):
    def post(self, request):
        user=User.objects.get(username="abi")
        list_permission=[ "edit_newsletter", "share_newsletter",
                          "unpublish_newsletter", "review_newsletter", "publish_newsletter"]
        permissions=Permission.objects.filter(codename__in=list_permission)
        for permission in permissions:
            user.user_permissions.add(permission)
        return Response({"message":"success"}, status=status.HTTP_200_OK)

    def get(self, request):
        user=User.objects.get(username="kiran")
        if user.has_perm('user_app.edit_newsletter'):
            print("user can edit newsletter")
        else:
            print("user cannot publish newsletter")
        if user.has_perm('user_app.publish_newsletter'):
            print("user can publish newsletter")
        else:
            print("user cannot publish newsletter")
        return Response({"message":"success"}, status=status.HTTP_200_OK)
    
class Publish_Newsletter_View(APIView):
    permission_classes=[IsAuthenticated, CanPublishNewsletter]
    
    def post(self, request):
        return Response({'message':'Newsletter published successfully'}, status=status.HTTP_200_OK)

class Check_Permissions(APIView):
    def get(self, request):
        user=User.objects.get(username='kiran')
        groups=[group.name for group in user.groups.all()]
        permission=[permission.codename for permission in user.user_permissions.all()]
        all_permissions=user.get_all_permissions()
        return Response({"username":user.username,
                         "groups":groups,
                         "direct_permissions":permission,
                         "all_permissions":all_permissions}, status=status.HTTP_200_OK)
    
class Check_Permissions_for_Group(APIView):
    def get(self, request):
        group=Group.objects.get(name='Editor')
        if group.permissions.filter(codename="publish_newsletter").exists():
            return Response({"group have this permission"}, status=status.HTTP_200_OK)
        return Response({"message":"group do not have this permission"}, status=status.HTTP_400_BAD_REQUEST)


class Set_User_In_Group(APIView):
    def post(self, request):
        group=Group.objects.get(name='Editor')
        user=User.objects.get(username='karthi')
        group.user_set.add(user)
        return Response({"message":"success"}, status=status.HTTP_200_OK)
    
    def get(self, request):
        groups=Group.objects.get(name='Editor')
        user_in_group=groups.user_set.all()
        for user in user_in_group:
            print(user.username)
        return Response({"message":"success"}, status=status.HTTP_200_OK)
        

# Fetch Groups for a User (auth_group + M2M Join)
from django.contrib.auth.models import Group

user=User.objects.get(username='karthi')
user_groups = Group.objects.filter(user=user)
for group in user_groups:
    print(group.name)

# Fetch Permissions for a Group (auth_group_permissions)
from django.contrib.auth.models import Permission

groups=Group.objects.get(name='Editor')
group_permissions = Permission.objects.filter(group=group)
for perm in group_permissions:
    print(perm.codename)

# Fetch Permissions for a User (auth_permission)
    
from django.contrib.auth.models import Permission

user=User.objects.get(username='karthi')
user_permissions = Permission.objects.filter(user=user)
for perm in user_permissions:
    print(perm.codename)
