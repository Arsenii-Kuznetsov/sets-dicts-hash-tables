from itertools import combinations

path = input(
    'Введите путь до файла, содержащего словарь в формате {студент1:{навык1,навык2},студент2:{навык1,навык2}}: ')
if not path.endswith('.txt'):
    exit('Файл должен иметь расширение txt')
try:
    with open(path, encoding='windows-1251') as file:
        students_and_skills = dict()
        line = file.readline()[1:-2]
        line = line.replace(':{', '{').replace('},', '{')
        line_split = line.split('{')
        for i in range(0, len(line_split), 2):
            students_and_skills[line_split[i]] = set(x for x in line_split[i + 1].split(','))
except FileNotFoundError:
    exit('Файл не найден')
except PermissionError:
    exit('Ошибка доступа')
skills_and_groups = dict()
for students, skills in students_and_skills.items():
    if tuple(skills) in skills_and_groups:
        skills_and_groups[tuple(skills)] += [students]
    else:
        skills_and_groups[tuple(skills)] = [students]
print('Группы студентов с одинаковыми навыками')
for skill in skills_and_groups:
    print(f'Группа с навыками {skill}: студенты: {skills_and_groups[skill]}')
superset_skills = set()
for student1, student2 in combinations(students_and_skills.keys(), 2):
    if students_and_skills[student1] > students_and_skills[student2]:
        superset_skills.add(student1)
    if students_and_skills[student1] < students_and_skills[student2]:
        superset_skills.add(student2)
print(f'Студенты, чьё множество навыков является надмножеством хотя бы для одного студента: {superset_skills}')
max_skills = max(len(skills) for skills in skills_and_groups.keys())
students_max_skills = set()
for skills in skills_and_groups:
    if len(skills) == max_skills:
        students_max_skills |= set(skills_and_groups[skills])
print(f'Студенты с самым большим количеством навыков: {students_max_skills}')
skills = list(students_and_skills.values())
similarity_matrix = [[0 for j in range(len(skills))] for i in range(len(skills))]
for i in range(len(skills)):
    for j in range(i, len(skills)):
        similarity_matrix[i][j] = float(f'{len(skills[i] & skills[j]) / len(skills[i] | skills[j]):.2f}')
        similarity_matrix[j][i] = similarity_matrix[i][j]
print('Матрица сходства навыков между всеми студентами')
indent = max(4, max(len(key) for key in students_and_skills.keys()))
students = list(students_and_skills.keys())
print(' '.join(f'{student:>{indent}}' for student in ([' '] + list(students_and_skills.keys()))))
for i in range(len(skills)):
    print(
        ' '.join(f'{element:>{indent}}' for element in ([students[i]] + [str(elem) for elem in similarity_matrix[i]])))
