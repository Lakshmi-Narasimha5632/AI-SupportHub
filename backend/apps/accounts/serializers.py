
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

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
