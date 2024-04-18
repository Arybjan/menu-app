from rest_framework import viewsets
from mn_app import models, serializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = models.Menu.objects.all()
    serializer_class = serializer.MenuSerializer
