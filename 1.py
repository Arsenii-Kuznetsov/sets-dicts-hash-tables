from itertools import combinations

path = input('Введите путь до файла: ')
if not path.endswith('.txt'):
    exit('Файл должен иметь расширение txt')
try:
    with open(path) as file:
        data_friends = file.readlines()
        friends = dict()
        for line in data_friends:
            line = line.replace('---', ' ')
            line_split = line.split()
            if line_split[0] in friends.keys():
                friends[line_split[0]].add(line_split[1])
            else:
                friends[line_split[0]] = {line_split[1]}
            if line_split[1] in friends.keys():
                friends[line_split[1]].add(line_split[0])
            else:
                friends[line_split[1]] = {line_split[0]}
except FileNotFoundError:
    exit('Файл не найден')
except PermissionError:
    exit('Ошибка доступа')
mutual_friends = []
for person1, person2 in combinations(friends.keys(), 2):
    if len(friends[person1] & friends[person2]) >= 2:
        mutual_friends += [(person1, person2)]
with open('result1.txt', 'w', encoding='windows-1251') as result:
    result.write(f'Пары людей, имеющих 2 и более общих друзей: {mutual_friends}')
