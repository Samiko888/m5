from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


from apps.users.models import Product
from apps.users.serializers import UserSerializer, UserRegisterSerializer

# Create your views here.
class ProductAPI(GenericViewSet,
              mixins.ListModelMixin, 
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        print(self.request.method == 'POST')
        if self.request.method == 'POST':
            return UserRegisterSerializer
        return UserSerializer 