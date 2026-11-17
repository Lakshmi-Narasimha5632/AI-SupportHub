
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

User = get_user_model()


class CustomerRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User

        fields = [
            'id',
            'full_name',
            'email',
            'password',
            'password2'
        ]

        read_only_fields = ['id']

    def validate_email(self, value):
        """
        Ensure email addresses are unique, ignoring case.
        """

        value = value.strip().lower()

        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                "An account with this email already exists."
            )

        return value

    def validate(self, attrs):
        """
        Check whether both password fields match.
        """

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                'password2': 'Passwords do not match.'
            })

        return attrs

    def create(self, validated_data):
        """
        Create a customer account securely.
        """

        validated_data.pop('password2')

        password = validated_data.pop('password')

        user = User.objects.create_user(
            password=password,
            role=User.Role.CUSTOMER,
            auth_provider=User.AuthProvider.EMAIL,
            **validated_data
        )

        return user


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)

    password = serializers.CharField(
        required=True,
        write_only=True,
        trim_whitespace=False
    )

    def validate(self, attrs):
        """
        Authenticate user using email and password.
        """

        email = attrs.get('email').strip().lower()
        password = attrs.get('password')

        # Authenticate using Django's authentication system
        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )

        if user is None:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "Your account is inactive. Contact support."
            )

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        attrs['user'] = user
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)

        return attrs



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only=True)

    def validate(self, attrs):
        self.token = attrs['refresh']

        try:
            self.refresh_token = RefreshToken(self.token)
        except TokenError:
            raise serializers.ValidationError({
                'refresh': 'Invalid or expired refresh token.'
            })

        return attrs

    def save(self, **kwargs):
        try:
            self.refresh_token.blacklist()
        except TokenError:
            raise serializers.ValidationError({
                'refresh': 'Unable to blacklist this token.'
            })

        return {
            'message': 'Logout successful.'
        }

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            'id',
            'full_name',
            'email',
            'role',
            'auth_provider',
            'is_active',
            'date_joined',
        ]

        read_only_fields = [
            'id',
            'email',
            'role',
            'auth_provider',
            'is_active',
            'date_joined',
        ]
