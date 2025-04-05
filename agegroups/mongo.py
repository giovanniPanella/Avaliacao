from django.conf import settings



db = settings.MONGO_DB
collection_agegroups = db.agegroups

def create_age_group(label, min_age, max_age=None):
    age_group = {
        "label": label,
        "min_age": min_age
    }
    if max_age is not None:
        age_group["max_age"] = max_age
    collection_agegroups.insert_one(age_group)

def delete_age_group(label):
    collection_agegroups.delete_one({"label": label})

def list_age_groups():
    return list(collection_agegroups.find({}, {"_id": 0}))

def get_all_age_groups():
    return list(collection_agegroups.find({}, {"_id": 0}))