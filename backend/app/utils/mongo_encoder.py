
from bson import ObjectId

def object_id_to_str(item):
    if isinstance(item, ObjectId):
        return str(item)
    elif isinstance(item, dict):
        return {k: object_id_to_str(v) for k, v in item.items()}
    elif isinstance(item, list):
        return [object_id_to_str(element) for element in item]
    else:
        return item