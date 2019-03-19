from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Language
from .serializers import LanguageSerializer

class LanguageViewSet(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer