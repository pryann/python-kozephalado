from json import load


json_file = open(file='MOCK_DATA.json', mode='r', encoding='utf-8')
json_data = load(json_file)
users = json_data['users']
# print(users)


def generate_id():
    return max(list(map(lambda user: user['id'], users))) + 1


def get_all_users():
    return users


def find_index(id):
    return users.index(find_user(id))


def find_user(id):
    return next((user for user in users if user['id'] == id), None)


def update_user(id, updated_user_data):
    index = find_index(id)
    users[index].update(updated_user_data)
    return users[index]


def create_users(user):
    new_user = user.copy()
    new_user.update({id: generate_id()})
    users.append(new_user)


def remove_user(id):
    user = find_user(id)
    users.remove(user)


print(find_user(1))
