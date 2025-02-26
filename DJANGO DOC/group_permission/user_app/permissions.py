from rest_framework.permissions import BasePermission

class CanPublishNewsletter(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('user_app.publish_newsletter')