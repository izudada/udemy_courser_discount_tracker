from django.urls import include, path
from rest_framework.routers import DefaultRouter

from discount_scrapper.views import DiscountViewset


router = DefaultRouter(trailing_slash=False)


router.register(
    r"course-discount",
    DiscountViewset,
    basename="course-discount",
)

urlpatterns = [path("", include(router.urls))]
