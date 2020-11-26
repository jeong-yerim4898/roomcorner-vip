from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token


app_name='accounts'

urlpatterns = [
    path('api-token-auth/',obtain_jwt_token),
    path('signup/',views.signup),
    path('<str:user_name>/',views.user_info),
    path('<str:user_name>/recommend/',views.user_recommend),  # 사용자별 영화 추천 받는 페이지
]
