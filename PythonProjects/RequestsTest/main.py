import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "39dcf65b52c7080255a2e4f27025d6ea"
HEADER = {"Content-Type" : "application/json", "trainer_token": TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "USER_LOGIN",
    "password": "USER_PASSWORD"
}          
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 18
}
body_change = {
    "pokemon_id": "74485",
    "name": "Pipo",
    "photo_id": 28
}
body_catch = {
"pokemon_id": "74485"
}

'''response = requests.post(url = f"{URL}/trainers/reg", headers = HEADER, json = body_registration) // регистрация тренера
print(response.text)'''

'''response_confirmation = requests.post(url = f"{URL}/trainers/confirm_email",headers = HEADER, json = body_confirmation) // подтверждение регистрации
print(response_confirmation.text)'''

'''response_create = requests.post(url = f"{URL}/pokemons",headers = HEADER, json = body_create) // создать покемона
print(response_create.text)'''

'''response_change = requests.put(url = f"{URL}/pokemons",headers = HEADER, json = body_change) // изменить инф. по покемону
print(response_change.text)'''

response_catch = requests.post(url = f"{URL}/trainers/add_pokeball",headers = HEADER, json = body_catch)
print(response_catch.text)







