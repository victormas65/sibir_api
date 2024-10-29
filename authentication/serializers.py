from rest_framework import serializers
from authentication.models import UserModel, RoleModel, UserModel
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate


class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = RoleModel
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)   # solo lo incluye cuando se graba o actualiza el registro

  class Meta:
    model = UserModel
    exclude = ('last_login', 'is_superuser')

  def save(self):
    if self.instance:
      instance = self.instance
      instance.first_name = self.validated_data.get('first_name')
      instance.last_name = self.validated_data.get('last_name')
      instance.email = self.validated_data.get('email')
      instance.status = self.validated_data.get('status')
      instance.role = self.validated_data.get('role')
      if 'password' in self.validated_data:
        instance.set_password(self.validated_data.get('password'))
      instance.save()
      return instance
    else:
      user = UserModel(**self.validated_data)
      user.set_password(self.validated_data.get('password'))
      user.save()
      return user
    
class LoginSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    print(attrs)
    user = authenticate(**attrs)
    if user and user.status:
      return super().validate(attrs)
    
    raise ValidationError('Usuario o contraseña incorrectos')

  def get_token(self, user):
    token = super().get_token(user)
    token['email'] = user.email
    token['first_name'] = user.first_name
    token['last_name'] = user.last_name
    return token
  

    




    