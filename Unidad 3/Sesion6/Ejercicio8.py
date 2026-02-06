import requests

endpoint = "https://dragonball-api.com/api/characters?limit=58"

try:
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()
    
    razas=[]
    for personaje in data["items"]:
           if personaje["race"] not in razas:
                razas.append(personaje["race"])


    for raza in razas:
        print(f"Lista de personajes de raza: {raza}")
        for personaje in data["items"]:
            if personaje["race"] == raza:
                print(f"- {personaje['name']}")

except requests.exceptions.RequestException as e:
    print(f"Error recuperando la data: {e}")