from jsonmodule import fetch_items

users = fetch_items('MOCK_DATA.json', 'users')


def get_all_users():
    return users


def find_user(id):
    for user in users:
        if user['id'] == id:
            return user
    return None


# print(get_all_users())
print(find_user(10))
