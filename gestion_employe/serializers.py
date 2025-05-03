from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """Serializer pour l'inscription d'un utilisateur."""

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}  # Le mot de passe ne sera pas renvoyé dans les réponses
        }

    def create(self, validated_data):
        """Créer un nouvel utilisateur avec les données validées."""
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
