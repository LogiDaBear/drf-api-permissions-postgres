from django.urls import path
from .views import CerealList, CerealDetail

urlpatterns = [
  path('', CerealList.as_view(), name='cereal_list'),
  path('<int:pk>', CerealDetail.as_view(), name='cereal_detail'),
]