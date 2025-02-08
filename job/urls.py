from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()


router.register(r'executors', ExecutorViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'order', OrderViewSet)
router.register(r'tag', TagViewSet)
router.register(r'ticket', TicketViewSet)
router.register(r'message', MessageViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'ordering', OrderingViewSet)
router.register(r'user', UserViewSet)


urlpatterns = router.urls
