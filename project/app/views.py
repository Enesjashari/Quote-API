from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer
from django.shortcuts import render

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

import random

import random
from django.http import JsonResponse

def random_quote_json(request):
    quote_count = Quote.objects.count()
    random_index = random.randint(0, quote_count - 1)
    random_quote = Quote.objects.all()[random_index]

    data = {
        "quote": random_quote.quote,
        "author": random_quote.author
    }
    return JsonResponse(data)

