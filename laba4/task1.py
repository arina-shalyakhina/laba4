# TODO решите задачу
import json
def task(filename) -> float:
    with open(filename) as file:
        data = json.load(file)
    a = []
    for i in data:
        for key, value in i.items():
            a.append(i.get('score') * i.get('weight'))
    c=list(set(a))
    return round(sum(c), 3)


print(task('input.json'))
