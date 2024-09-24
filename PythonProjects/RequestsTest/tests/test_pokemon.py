import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "39dcf65b52c7080255a2e4f27025d6ea"
HEADER = {"Content-Type" : "application/json", "trainer_token": TOKEN}
TRAINER_ID = "6323" 

def test_statys_code():
    response = requests.get(url = f"{URL}/pokemons", params = {"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f"{URL}/pokemons", params = {"trainer_id" : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_id"] == "6323"
   
