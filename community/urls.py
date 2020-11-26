from django.urls import path
from . import views

app_name='community'

urlpatterns = [
    path('',views.community_list_create),
    path('<int:community_pk>/',views.community_update_delete),
    path('<int:community_pk>/comment/', views.comment_list_create),
    path('<int:community_pk>/comment/<int:communitycomment_pk>/', views.comment_delete_update),
]
