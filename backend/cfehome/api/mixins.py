from rest_framework import permissions

from .permissions import IsStaffEditorPermission

#Mixin keyword at the end specifies that it is mixin class.
class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]