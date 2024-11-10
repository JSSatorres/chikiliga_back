from bson import ObjectId

def transform_object_id(document):
    """Convierte ObjectId en un string dentro del documento."""
    if "_id" in document and isinstance(document["_id"], ObjectId):
        document["_id"] = str(document["_id"])
        return document
    