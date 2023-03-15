from typing import Any, Dict

from .choices import FoodCategoryChoices

FIELD_CHOICE_MAP: Dict[str, Any] = {"category": FoodCategoryChoices}


def get_choices_error_message(field) -> str:
    choices = FIELD_CHOICE_MAP[field]
    choices_str = ", ".join(
        [f"{choices[member].name}: {choices[member].value}" for member in choices.__members__]
    )
    message = f"Valid choices are: {choices_str}"
    return '"{input}" is not a valid choice. ' + message
