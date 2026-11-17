
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CustomerRegistrationSerializer

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import LoginSerializer
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle
class CustomerRegistrationView(generics.CreateAPIView):

    serializer_class = CustomerRegistrationSerializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(
            {
                "message": "Customer registered successfully.",
                "user": {
                    "id": user.id,
                    "full_name": user.full_name,
                    "email": user.email,
                    "role": user.role
                }
            },
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):

    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle, ScopedRateThrottle]
    throttle_scope = 'login'
    def post(self, request):

        # Validate login credentials
        serializer = LoginSerializer(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        # Prepare successful login response
        response_data = {
            "message": "Login successful",

            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role,
            },

            "tokens": {
                "access": serializer.validated_data['access'],
                "refresh": serializer.validated_data['refresh'],
            }
        }

        return Response(
            response_data,
            status=status.HTTP_200_OK
        )
