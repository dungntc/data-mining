from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.template.response import TemplateResponse
from data_mining.labelling.models import Label
from random import randint
from data_mining.labelling.management.commands import run
import json

def home(request):
    return TemplateResponse(request, 'home.html')

@api_view(['GET'])
def getAllLabels(request):
    all_label = Label.objects.all()
    bad_label = Label.objects.all().filter(is_good = 0)
    return JsonResponse({
        'all': len(all_label) ,
        'bad': len(bad_label) ,
        'status': True
    }, status=200)

@api_view(['GET'])
def getOneLabel(request):
    bad_label = Label.objects.all().filter(is_good = 0)
    random_index = randint(0, len(bad_label) - 1)
    result = bad_label[random_index]
    return JsonResponse({
        'result': {
            'id': result.id,
            'line': result.line ,
            'option1': result.option1,
            'option2': result.option2,
            'option3': result.option3,
            'option4': result.option4,
            'content': result.content,
            'is_good' : result.is_good,
            'result' : str(result.result)
        },
        'status': True
    }, safe=False, json_dumps_params={'ensure_ascii': False}, status =200)

@api_view(['POST'])
def update(request):
    data_body =json.loads(request.body.decode('utf-8'))
    line = data_body.get('line', None)
    result = data_body.get('result', None)
    if line is None and result is None:
        return JsonResponse({
            'data': 'Value is None',
            'status': False
        }, status=400)
    label = Label.objects.all().filter(line=line)[0]
    label.is_good = 1
    label.result =result
    label.save()
    return JsonResponse({
        'data': 'OK',
        'status': True
    }, status= 200)

@api_view(['GET'])
def runCommand(request):
    try:
        cmd= globals()['run'].Command()
        cmd.handle()
    except Exception as e:
        return JsonResponse({
            'data': 'server error: '+str(e),
            'status':False
        }, status=500)
    label = Label.objects.all()
    return JsonResponse({
        'data': 'oke',
        'status': True
    }, status=200)
