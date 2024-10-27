import requests
from django.core.exceptions import ValidationError


def validate_breed(value):
    try:
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        response.raise_for_status()
        breeds_data = response.json()
        breed_names = [breed["name"] for breed in breeds_data]
        
        if value not in breed_names:
            raise ValidationError(f"{value} is not a valid breed.")
    except requests.RequestException as e:
        raise ValidationError("Could not validate breed due to an API error.")
