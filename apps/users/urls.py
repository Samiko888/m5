from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPI
from apps.products.views import ProductAPI
from apps.categories.views import categoriesAPI

router = DefaultRouter()
router.register('users', UserAPI, 'api_user')
router.register('products', ProductAPI, 'api_product')
router.register('categories',categoriesAPI, 'api_categories' )

urlpatterns = router.urls 

