from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profile_rest_api_app.serializers import NameField,MyUserSerializers
from profile_rest_api_app import models

# Create your views here.

class HelloView(APIView):
    ''' Defining API Views '''

    def get(self,request,format=None):
        """This is a get request method"""

        string="Hello welcome to API View"
        list=[
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
            ]

        return Response({"string":string,"list":list})


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


    def put(self,request):
        """Create a PUT request """
        return Response({"message":"Peforming PUT request"})


    def patch(self,request):
        """Create a Patch Request"""
        return Response({"message":"Performing Patch request"})


    def delete(self,request):
        """Create a Delete request"""
        return Response({"message":"Performing a Delete request"})

class HelloViewSet(viewsets.ViewSet):
    """ Defining Viewsets """

    def list(self,request):
        """This acts as get reqest"""
        api_listviewset=[
        "Viewset is another way to write logic to a API",
        "We don't use method names same as the http methods",
        "We use method name list() which acts a get methods"
        ]

        return Response({"message":"hello viewsets","api_listviewset":api_listviewset})


    serializer_class=NameField      # this is a fixed way to declare serializers
    def create(self,request):
        """ this acts as a Post request"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get("name")
            return Response({"name":f"My name is {name}"})
        else:
            return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk=None):
        """this acts as a get request for a particular object.
           pk is mandatory as a primary key for the object """
        return Response({"message":"GET request"})


    def update(self,request,pk=None):
        """this acts a put request for a particular object
           pk is mandatory as a primary key for the object """
        return Response({"message":"PUT request"})

    def partial_update(self,request,pk=None):
        """this acts a patch request for a particular object
           pk is mandatory as a primary key for the object """
        return Response({"message":"Patch request"})

    def destroy(self,request,pk=None):
        """this acts a delete request for a particular object
           pk is mandatory as a primary key for the object """
        return Response({"message":"Delete request"})

class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class=MyUserSerializers
    queryset=models.MyUser.objects.all()
