from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_rest_api_app.serializers import NameField

# Create your views here.

class HelloView(APIView):
    ''' API view tutorial '''

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
