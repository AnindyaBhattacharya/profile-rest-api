from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()      # create a DefaultRouter object.
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")
router.register("user-profile", views.UserProfileViewset, base_name="user-profile")
router.register("user-feed", views.UserStatusFeedView, base_name="user-profile")


# with router.register we register urls for all the functions defined inside the viewset class.
# hello_viewset will contain all the four urls for - list,create,retreive,update,partial_update,destroy
# we need not to explicitly define urls for each of those methods.

urlpatterns = [
    path('hello_apiview', views.HelloView.as_view()),
    path('', views.UserLoginView.as_view()),
    # we include the list of urls generated in router.urls
    path('', include(router.urls)),
]
