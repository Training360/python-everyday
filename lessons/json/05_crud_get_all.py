from jsonmodule import fetch_items

users = fetch_items('MOCK_DATA.json', 'users')


def get_all_users():
    return users


print(get_all_users())
