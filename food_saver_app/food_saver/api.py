from food import views as food_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"products", food_views.ProductViewSet)
router.register(r"quantities", food_views.QuantityViewSet)
