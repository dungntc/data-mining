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

@api_view(['GET'])
def get1(request):

    Lines = [41 ,77 ,133 ,149 ,293 ,367 ,380 ,557 ,625 ,988 ,1022 ,1025 ,1152 ,1169 ,1196 ,1249 ,1252 ,1260 ,1326 ,1405 ,1490 ,1506 ,1536 ,1546 ,1585 ,1590 ,1637 ,1699 ,1721 ,1758 ,1800 ,1815 ,1898 ,1917 ,2081 ,2131 ,2385 ,2395 ,2399 ,2403 ,2456 ,2646 ,2647 ,2747 ,2844 ,2907 ,2909 ,2933 ,3145 ,3218 ,3393 ,3412 ,3502 ,3559 ,3588 ,3614 ,3633 ,3663 ,3718 ,3755 ,3928 ,4142 ,4143 ,4161 ,4220 ,4226 ,4551 ,4564 ,4681 ,4740 ,4745 ,4819 ,5088 ,5300 ,5373 ,5425 ,5470 ,5487 ,5598 ,5712 ,5780 ,5885 ,6045 ,6051 ,6090 ,6105 ,6171 ,6220 ,6389 ,6397 ,6406 ,6626 ,6639 ,6809 ,6817 ,6844 ,6862 ,7127 ,7130 ,7151 ,7178 ,7193 ,7217 ,7246 ,7515 ,7572 ,7698 ,7716 ,7725 ,7737 ,7776 ,7855 ,7900 ,7909 ,7916 ,7974 ,7978 ,7983 ,8029 ,8055 ,8114 ,8128 ,8331 ,8358 ,8517 ,8632 ,8666 ,8710 ,8819 ,8854 ,8982 ,8999 ,9134 ,9230 ,9313 ,9348 ,9350 ,9400 ,9484 ,9515 ,9543 ,9785 ,9982]
    bad_label = Label.objects.all().filter(line__in=Lines)
    resulf = []
    resulf = [{'line': l.line, 'label': l.result}
                    for l in bad_label]
    return JsonResponse({
        'length' : len(resulf),
        'result': resulf,
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

@api_view(['GET'])
def run1(request):
    bad_label = Label.objects.all().filter(is_good=0)
    print(len(bad_label))
    for label in bad_label:
        if label.option1 == label.option2 and label.option1 == label.option3:
            label.result = label.option1
            label.is_good = 1
            label.save()

        if label.option1 == label.option2 and label.option1 == label.option4:
            label.result = label.option1
            label.is_good = 1
            label.save()

        if label.option1 == label.option3 and label.option1==label.option4:
            label.result = label.option1
            label.is_good = 1
            label.save()

        if label.option3 == label.option2 and label.option2==label.option4:
            label.result = label.option2
            label.is_good = 1
            label.save()

    return JsonResponse({
        'data': 'oke',
        'status': True
    }, status=200)

