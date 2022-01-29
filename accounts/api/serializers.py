from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Account
        fields = ["email", "username", "password", "password2"]
        extra_kwargs = {'password': {"write_only": True}}

    def save(self):
        user = Account(email=self.validated_data["email"],
                       username=self.validated_data["username"])

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password2 == password:
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'password': 'Passwords must match.'})


class UserInformation(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "email", "username"]

