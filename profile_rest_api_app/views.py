from rest_framework.views import APIView
from rest_framework.response import Response
# to set a HTTP status request.
from rest_framework import status
# to define a restapi views in form of view sets
from rest_framework import viewsets
# for assigning an Authentication type
from rest_framework.authentication import TokenAuthentication
# to set search filters in Rest API
from rest_framework import filters
# for generating an Authentication Tocken
from rest_framework.authtoken.views import ObtainAuthToken
# for setting the renderer_classes require for login page
from rest_framework.settings import api_settings
# for accessign inbuilt permission settings. IsAuthenticatedOrReadOnly and IsAuthenticated.
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# custom defined imports.
from profile_rest_api_app.serializers import (
    NameField, MyUserSerializers,
    UserStatusFeedSerializer)
from profile_rest_api_app import models, permissions


# Create your views here.


class HelloView(APIView):
    ''' Defining API Views '''

    def get(self, request, format=None):
        """This is a get request method"""

        string = "Hello welcome to API View"
        list = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({"string": string, "list": list})

    serializer_class = NameField

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        """Create a PUT request """
        return Response({"message": "Peforming PUT request"})

    def patch(self, request):
        """Create a Patch Request"""
        return Response({"message": "Performing Patch request"})

    def delete(self, request):
        """Create a Delete request"""
        return Response({"message": "Performing a Delete request"})


class HelloViewSet(viewsets.ViewSet):
    """ Defining Viewsets """

    def list(self, request):
        """This acts as get reqest"""
        api_listviewset = [
            "Viewset is another way to write logic to a API",
            "We don't use method names same as the http methods",
            "We use method name list() which acts a get methods"
        ]

        return Response({"message": "hello viewsets", "api_listviewset": api_listviewset})

    serializer_class = NameField      # this is a fixed way to declare serializers

    def create(self, request):
        """ this acts as a Post request"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            return Response({"name": f"My name is {name}"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """this acts as a get request for a particular object.
           pk is mandatory as a primary key for the object """
        return Response({"message": "GET request"})

    def update(self, request, pk=None):
        """this acts a put request for a particular object
           pk is mandatory as a primary key for the object """
        return Response({"message": "PUT request"})

    def partial_update(self, request, pk=None):
        """this acts a patch request for a particular object
           pk is mandatory as a primary key for the object """
        return Response({"message": "Patch request"})

    def destroy(self, request, pk=None):
        """this acts a delete request for a particular object
           pk is mandatory as a primary key for the object """
        return Response({"message": "Delete request"})


class UserProfileViewset(viewsets.ModelViewSet):
    '''
    Extending to ModelViewSet ensures that all the viewsets methods are taken care of.
    We need not to explicitly define list,create,retrieve,update,partial_update,destroy functions.
    ModelViewSets handles and executes those methods.
    We need to define the below sets of class variables. The name of the varibles should not be changed.
    '''
    # define serializer class.
    # The serializer class that should be used for validating and deserializing input, and for serializing output
    serializer_class = MyUserSerializers
    # define a queryset containing all objects.
    # The queryset that should be used for returning objects from this view.
    queryset = models.MyUser.objects.all()
    # define the type of authentication we want to perform.
    authentication_classes = (TokenAuthentication,)
    # define the permissions to be given to once authenticated. Permissions are defined in permissions.py file.
    permission_classes = (permissions.CustomPermission,)
    # create a filter for easy search of model objects.
    # A list of filter backend classes that should be used for filtering the queryset
    filter_backends = (filters.SearchFilter,)
    # create fields on which we want to perform search operation.
    search_fields = ('email', 'username')


class UserLoginView(ObtainAuthToken):
    '''
    Class is used to display a login page in the api framewok
    To get a display login page we create UserLoginView class extending ObtainAuthToken.
    Inside class we need to define a renderer_classes class variable and assign setting for making a login page.
    Add this class in urls.py to create an end-point for a login page.
    '''
    # Assigning the DEFAULT_RENDERER_CLASSES settings, which creates a loging page
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserStatusFeedView(viewsets.ModelViewSet):
    '''
    Creating a viewset by extending ModelViewSets, which in turn takes care of all viewset methods
    Declaring the class level variables.
    Overriding perform_create function to save the serializer for a paricular object.
    '''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserStatusFeedSerializer
    queryset = models.UserStatusFeed.objects.all()
    permission_classes = (permissions.StatusFeedPermission, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        '''
        Called by CreateModelMixin when saving a new object instance.
        For instance, you might set an attribute on the object based on the request user.
        Overriding the function so that it can save values for a particular user instance.
        similar methods - perform_update(self, serializer),perform_destroy(self, instance)
        '''
        # Saves the serializer values for a particular user.
        serializer.save(user_profile_id=self.request.user)
