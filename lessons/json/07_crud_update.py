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


# print(get_all_users())
# print(find_user(10))
print(update_user(1, {'first_name': 'Gergely', 'last_name': 'Gáll'}))
