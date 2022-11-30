# работал со swagger для petfriends.skillfactory.ru/, взял из Slack
import json
import requests
print('___________________')
print('get_api_key')
header_key = {'email': 'ivanovskyr@yandex.ru',
          'password': 'Qw123456',
          'accept': 'application/json'}
r = requests.get('https://petfriends.skillfactory.ru/api/key', headers = header_key)
print(r.json())
auth_key = r.json()['key']
print('___________________')
print('post_create_pet_simple')
header = {'auth_key': auth_key,
        'accept': 'application/json'}
data = {'name': 'Филипп',
        'animal_type': 'Кот',
        'age': '7'}
res = requests.post('https://petfriends.skillfactory.ru/api/create_pet_simple', headers = header, data = data)
if 'application/json' in res.headers['Content-Type']:
    print(f'Вывод json {res.json()}')
else:
    print(f'Вывод text {res.text}')
pet_id = res.json()['id']
print('___________________')
print('get_pets')
filter = 'my_pets'
res = requests.get(f'https://petfriends.skillfactory.ru/api/pets?filter={filter}', headers = header)
if 'application/json' in res.headers['Content-Type']:
    print(f'Вывод json с моими животными: {res.json()}')
else:
    print(f'Вывод text с моими животными: {res.text}')
print('___________________')
print('post_pets')
data1 = {'name': 'Филька',
        'animal_type': 'Котяра',
        'age': '8',
        'pet_photo': ''}
res = requests.post('https://petfriends.skillfactory.ru/api/create_pet_simple', headers = header, data = data1)
if 'application/json' in res.headers['Content-Type']:
    print(f'Вывод json с добавленным животным: {res.json()}')
else:
    print(f'Вывод text с добавленным животным: {res.text}')
print('___________________')
print('PUT_api_pets')
data2 = {'name': 'Зверюга',
        'animal_type': 'котик',
        'age': '3',
        'pet_photo': ''}
res = requests.put(f'https://petfriends.skillfactory.ru/api/pets/{pet_id}', headers = header, data = data2)
if 'application/json' in res.headers['Content-Type']:
    print(f'Вывод json с обновленным животным: {res.json()}')
else:
    print(f'Вывод text с обновленным животным: {res.text}')
print('___________________')
print('delete_pet_id')
header = {'auth_key': auth_key,
        'accept': 'application/json'}
res = requests.delete(f'https://petfriends.skillfactory.ru/api/pets/{pet_id}', headers = header)
print(f'Код выполнения запроса DELETE: {res.status_code}')