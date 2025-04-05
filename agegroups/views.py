from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .mongo import create_age_group, delete_age_group, list_age_groups




@csrf_exempt

def add_age_group(request):
    if request.method == "POST":
        data = json.loads(request.body)
        label = data.get("label")
        min_age = data.get("min_age")
        max_age = data.get("max_age")

        if not label or min_age is None:
            return JsonResponse({"erro": "label e min_age são obrigatórios"}, status=400)

        create_age_group(label, min_age, max_age)
        return JsonResponse({"mensagem": "Faixa etária criada com sucesso!"})

    return JsonResponse({"erro": "Método não permitido"}, status=405)

@csrf_exempt

def remove_age_group(request):
    if request.method == "DELETE":
        data = json.loads(request.body)
        label = data.get("label")

        if not label:
            return JsonResponse({"erro": "label é obrigatório"}, status=400)

        delete_age_group(label)
        return JsonResponse({"mensagem": "Faixa etária removida com sucesso!"})

    return JsonResponse({"erro": "Método não permitido"}, status=405)


def get_age_groups(request):
    if request.method == "GET":
        age_groups = list_age_groups()
        return JsonResponse(age_groups, safe=False)

    return JsonResponse({"erro": "Método não permitido"}, status=405)
