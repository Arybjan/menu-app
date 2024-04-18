from rest_framework.routers import DefaultRouter
from mn_app import views


router = DefaultRouter()

router.register("menu_selection", views.MenuViewSet)

urlpatterns = router.urls
