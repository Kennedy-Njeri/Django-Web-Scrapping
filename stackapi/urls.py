from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from .views import index, QuestionAPI, latest
from rest_framework import routers

router = routers.DefaultRouter()
router.register("question", QuestionAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('latest', latest, name="latest")

]
