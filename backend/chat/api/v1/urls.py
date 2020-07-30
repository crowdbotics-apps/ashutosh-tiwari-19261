from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    MessageViewSet,
    ThreadMemberViewSet,
    MessageActionViewSet,
    ThreadActionViewSet,
    ForwardedMessageViewSet,
    ThreadViewSet,
)

router = DefaultRouter()
router.register("threadaction", ThreadActionViewSet)
router.register("message", MessageViewSet)
router.register("threadmember", ThreadMemberViewSet)
router.register("thread", ThreadViewSet)
router.register("forwardedmessage", ForwardedMessageViewSet)
router.register("messageaction", MessageActionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
