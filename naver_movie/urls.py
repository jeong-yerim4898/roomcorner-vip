from django.urls import path
from . import views

app_name='naver_movie'

urlpatterns = [
    path('',views.movies),
    path('<int:movie_pk>/comment/', views.comment_list_create),
    path('<int:movie_pk>/comment/<int:comment_pk>/', views.comment_delete_update),
    path('corona/',views.corona_info),
]
