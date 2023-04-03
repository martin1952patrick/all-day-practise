from django.http import JsonResponse
from .models import Drink
from .serializers import    DrinkSerializer

def drink_list(request):
    
    #1.get all the drinks
    #2.serialize them
    #3.return json

   drinks =  Drink.objects.all() 
   serializer = DrinkSerializer(drinks, many = True)
   return JsonResponse({"drinks":serializer.data}, safe =  False)
     