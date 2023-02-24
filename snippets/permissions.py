from rest_framework import permissions


# Custom permission to only allow owners of an object to edit it
class IsOwnerOrReadOnly(permissions.BasePermission):
	
	# Read permissions are allowed to any request, write permissions are only allowed to
	# the owner of the snippet, so we'll always allow GET, HEAD or OPTIONS requests
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.owner == request.user
