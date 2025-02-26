from django.urls import path
from .views import (Group_View, User_Create, Permission_view, 
                    Group_Permission_View, User_Permission_view,
                    User_Group_Add_View, Check_Permissions,
                    Set_User_In_Group)
urlpatterns=[
    path("create/group/",Group_View.as_view(), name="create group"),
    path("create/user/", User_Create.as_view(), name="User Create"),
    path("create/permission/", Permission_view.as_view(), name="create permission"),
    path("list/permission/",Permission_view.as_view(), name="list permission"),
    path("delete/permissions/", Permission_view.as_view(), name="delete permissions"),
    path("add/group/permission/", Group_Permission_View.as_view(), name="add group permission"),
    path("add/user/permissions", User_Permission_view.as_view(), name="add user permission"),
    path("add/user/group/", User_Group_Add_View.as_view(), name="Add User to Group"),
    path("check/permissions/", Check_Permissions.as_view(), name="check permission"),
    path("set/user-in-group/", Set_User_In_Group.as_view(), name="set user in group")
]