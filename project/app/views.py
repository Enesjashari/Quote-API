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

def contribute(request):
    quote = request.POST.get("quote")
    if quote:
        movie_title  = request.POST.get("movie_title",'Null')        
        actor_name   = request.POST.get("actor_name",'Null')        
        category     = request.POST.get("category",'Null')        
        publish_date = request.POST.get("publish_date",'Null')            
        source       = request.POST.get("source",'Null')    
        context      = request.POST.get("context",'Null')    
        rating       = request.POST.get("rating",'Null')    
        language     = request.POST.get("language",'Null')        
        author       = request.POST.get("author",'Null')    
        author_bio   = request.POST.get("author_bio",'Null')        
        adding = Quote(quote=quote,movie_title = movie_title , actor_name = actor_name , 
                    category=category,publish_date = publish_date , source=source
                    ,context=context,rating=rating,language=language,
                    author=author,author_bio=author_bio)
        adding.save()
    
    return render(request,"contribute.html")


def index(request):
    return render(request,'index.html')