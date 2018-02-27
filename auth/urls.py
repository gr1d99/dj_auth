from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token


urlpatterns = [
    url(r'^api-auth-token/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]