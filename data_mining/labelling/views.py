from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def getAllLabels(request):
    return JsonResponse({
        'data': 'oke',
        'status': True
    }, status=200)