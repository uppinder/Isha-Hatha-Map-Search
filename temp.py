import json

with open('teachers.json', 'r') as f:
    teachers = json.load(f)

for teacher in teachers:
    if teacher['cities'][0]['name'].count(',') > 2:
        print(teacher['name'])