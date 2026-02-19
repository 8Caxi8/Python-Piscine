def validate_ingredients(ingredients: str) -> str:
    known_ingredients: set[str] = {
        "fire", "water", "earth", "air"
    }

    if set(ingredients.split()).issubset(known_ingredients):
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
