from rest_framework import permissions

# define custom permissions


class CustomPermission(permissions.BasePermission):
    '''
    Class is used to define custom permissions.
    This class allows only authenticated user to modify their own field.
    Authentication is performed by TokenAuthentication method.
    Before Token Authentication users are Anonymous users.
    After Token Authenticaton a particular user is identified.
    '''

    def has_object_permission(self, request, view, obj):
        '''
        SAFE_METHODS are non destructive methods. Like get methods. Anonymous users have access to SAFE_METHODS
        Once verified and is identified that user is tryring to access his own fields it allows to perform Put,Patch,Delete.
        Else it only allows to perform SAFE_METHODS like get operations.
        Before token authentication [request.user] returns Anonymous users
        After token authentication [request.user] returns anindya@admin.com
        '''
        print((request.data))
        print(view)
        print(obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        # print("value of request.user.id :-", request.user)    AnonymousUser(without auth),anindya@admin.com(with auth)
        return obj.id == request.user.id  # if False then only access to SAFE_METHODS


class StatusFeedPermission(permissions.BasePermission):
    '''
    Defining a permission class for custom permissions.
    This class allows only authenticated user to modify their own field.
    '''

    def has_object_permission(self, request, view, obj):
        '''
        If authenticated and user's id and object's id are same then all methods are accessible
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile_id.id == request.user.id
