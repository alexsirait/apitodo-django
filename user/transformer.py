def transform(values):
    arr = []

    for item in values:
        arr.append(singleTransform(item))

    return arr


def singleTransform(values):
    return {
        "id": values.id,
        "name": values.name,
        "email": values.email,
        "created_at": str(values.created_at),
        "updated_at": str(values.updated_at)
    }