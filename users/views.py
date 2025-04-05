from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .mongo import save_user, list_users as list_users_from_mongo
from agegroups.mongo import get_all_age_groups
from .mongo import collection_users

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if "name" not in data or "cpf" not in data or "age" not in data:
            return JsonResponse({"erro": "Campos nome, cpf e idade são obrigatórios"}, status=400)
            cpf = data["cpf"]
            existing_user = collection_users.find_one({"cpf": cpf})
            if existing_user:
                return JsonResponse({"erro": "CPF já está cadastrado!"}, status=400)


        if save_user(data):
            return JsonResponse({"mensagem": "Usuário cadastrado com sucesso!"})
        else:
            return JsonResponse({"erro": "Idade fora dos grupos cadastrados"}, status=400)

    return JsonResponse({"erro": "Método não permitido"}, status=405)

def list_users(request, track):
    if request.method == "GET":
        users = list_users_from_mongo(track)
        for user in users:
            user.pop("cpf", None)

        return JsonResponse(users, safe=False)

    return JsonResponse({"erro": "Método não permitido"}, status=405)

def user_status(request, cpf):
    if request.method == "GET":
        user = collection_users.find_one({"cpf": cpf})
        if not user:
            return JsonResponse({"erro": "Usuário não encontrado"}, status=404)

        age = user.get("age", 0)
        track = None

        
        age_groups = get_all_age_groups()
        for group in age_groups:
            min_age = group.get("min_age")
            max_age = group.get("max_age")
            name = group.get("label")

            if max_age is None and age >= min_age:
                track = name
                break
            elif min_age <= age <= max_age:
                track = name
                break

        return JsonResponse({
            "name": user.get("name"),
            "cpf": user.get("cpf"),
            "age": age,
            "track": track or "Não classificado"
        })

    return JsonResponse({"erro": "Método não permitido"}, status=405)