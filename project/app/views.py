from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer



from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_quotes(request):
    members = Quote.objects.all()
    serialized_members = QuoteSerializer(members, many=True).data
    data = {'Quotes': [serialized_members]}
    return Response(data)
