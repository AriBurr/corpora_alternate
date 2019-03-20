from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import RecommenderService

class RecommenderView(APIView):
    def get(self, request):
        substrings = RecommenderService.get_all_permutations(request.data)
        response = RecommenderService.search_substrings(substrings)
        return Response(response, status=status.HTTP_201_CREATED)
