def noteEntity(item) -> dict:
    return {
        "id": str(item.get("_id")),  # Safe extraction of '_id'
        "title": item.get("title", "Untitled"),  # Default to "Untitled" if missing
        "description": item.get("description", "No description"),  # Default to "No description"
        "important": item.get("important", False)  # Default to False if missing
    }

def noteEntities(items) -> list:
    return [noteEntity(item) for item in items]
