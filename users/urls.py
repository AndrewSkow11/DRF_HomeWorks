from rest_framework import routers

from users.views import UsersAPIViewSet

router = routers.SimpleRouter()
router.register('users', UsersAPIViewSet)

urlpatterns = [] + router.urls
