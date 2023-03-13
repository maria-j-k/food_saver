from rest_framework import routers
from food import views as food_views

router = routers.DefaultRouter()
router.register(r"products", food_views.ProductViewSet)