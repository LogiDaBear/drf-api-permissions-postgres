from rest_framework import generics
from .serializer import CerealSerializer
from .models import Cereal
from .permissions import IsOwnerOrReadOnly

class CerealList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Cereal.objects.all()
  serializer_class = CerealSerializer
  
class CerealDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Cereal.objects.all()
  serializer_class = CerealSerializer