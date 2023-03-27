from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the author of the snippet.
		return obj.author == request.user


class IsStaffOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		# print(request.user, request.method)
		if request.method in permissions.SAFE_METHODS:
			# The method is a safe method
			# print('safe')
			return True
		else:
			# The method isn't a safe method
			# Only owners are granted permissions for unsafe methods
			return request.user.is_staff