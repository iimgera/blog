from rest_framework.routers import DefaultRouter
from user.views import RegistrUserView


router = DefaultRouter()

router.register('users', RegistrUserView, basename='users')


urlpatterns = router.urls
