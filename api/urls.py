from rest_framework import routers

from .views import TodoViewSet, ResumeViewSet

router = routers.SimpleRouter()
router.register(r'todos', TodoViewSet)
router.register(r'resumes', ResumeViewSet)

urlpatterns = router.urls
