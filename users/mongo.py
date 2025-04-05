
from django.conf import settings

db = settings.MONGO_DB
collection_users = db.users
collection_agegroups = db.agegroups
collection_users.create_index("cpf", unique=True)

def save_user(data):
    """Salva um usuário no MongoDB após validar a idade"""
    age = data.get("age")
 
 
    age_group = collection_agegroups.find_one({
        "$or": [
            {"min_age": {"$lte": age}, "max_age": {"$gte": age}},
            {"min_age": {"$lte": age}, "max_age": {"$exists": False}}
        ]
    })

    if not age_group:
        return False  # Indica falha

    collection_users.insert_one(data)
    return True  # Indica sucesso

def list_users(etaria):
    """Filtra usuários conforme faixa etária"""
    track = {
        "18-25": {"age": {"$gte": 18, "$lte": 25}},
        "26-35": {"age": {"$gte": 26, "$lte": 35}},
        "36-45": {"age": {"$gte": 36, "$lte": 45}},
        "46+": {"age": {"$gte": 46}},
    }
    filter = track.get(etaria)
    if not filter:
        return []
    return list(collection_users.find(filter, {"_id": 0}))
