import json

def create_account(user):
    with open('fixtures/users.json', 'r') as file:
        users = json.loads(file.read())

    users.append(user.to_dict())

    with open('fixtures/users.json', 'w') as file:
        file.write(json.dumps(users, indent=4, separators=(',', ': ')))
