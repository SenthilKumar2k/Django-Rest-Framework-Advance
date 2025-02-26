"""Creating a permission list in Django involves defining permissions either through code or 
the database

Step 1: Permissions in Django
Default Permissions: Django automatically creates the following permissions for each model:

add_<modelname>
change_<modelname>
delete_<modelname>
view_<modelname> (if view is enabled in Meta).

Step 2: Custom Permissions: 
You can define your own permissions in the Meta class of a model.
"""

"""Superusers can perform any action in the Django admin interface or custom permission 
checks in your code.There's no need to explicitly assign permissions to a superuser—they 
have all permissions by default."""

"""
Using Permissions in the Admin Panel
# Permissions are visible in the Django Admin under Users and Groups.
# You can manually assign permissions via the admin interface.
"""

"""
Summary
#  Permissions are stored in the auth_permission table.
#  Use the Permission model to list, create, or manage permissions.
#  Permissions can be assigned to users or groups and checked dynamically using methods like has_perm.
"""




