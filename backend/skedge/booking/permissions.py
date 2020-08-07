from rest_framework import permissions


class IsCustomerOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user

class IsBusinessOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.business = request.user
