from jsonmodule import fetch_items

users = fetch_items('MOCK_DATA.json', 'users')


def get_all_users():
    return users


def find_user(id):
    for user in users:
        if user['id'] == id:
            return user
    return None


def update_user(id, updated_user):
    index = users.index(find_user(id))
    if index is not None:
        users[index].update(updated_user)
    return users[index]


def create_user(user):
    new_user = user.copy()
    new_user.update({'id': users[-1]['id'] + 1})
    users.append(new_user)
    return new_user


def remove_user(id):
    user = find_user(id)
    users.remove(user)


# print(get_all_users())
# print(find_user(10))
# print(update_user(1, {'first_name': 'Gergely', 'last_name': 'Gáll'}))
# print(create_user({'first_name': 'Johnny', 'last_name': 'Boy'}))
remove_user(1)
print(find_user(1))
