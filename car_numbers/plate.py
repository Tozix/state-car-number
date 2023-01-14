import json
from random import choices, randint

LETTERS = 'ABEKMHOPCTYX'


def gen_number_plate():
    letters = ''.join(choices(LETTERS, k=1))
    numbers = randint(1, 999)
    return f'{letters}{numbers:03d}{letters}{letters}'


amount = 10
plates = []
for i in range(amount):
    plates.append(gen_number_plate())

data = {
    "plates": plates
}
data = {'plates': [*plates]}
print('DATA', data)
data = json.dumps(data)
print(data)
