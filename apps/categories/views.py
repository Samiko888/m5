
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


from apps.categories.models import Categories
from apps.categories.serializers import CategoriesSerializer

# Create your views here.
class categoriesAPI(GenericViewSet,
              mixins.ListModelMixin, 
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

