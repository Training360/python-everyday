import requests
import json

base_url = "https://jsonplaceholder.typicode.com"

def get_all(endpoint):
    url = f"{base_url}/{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None
    
def find_data(endpoint, id):
    url = f"{base_url}/{endpoint}/{id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None

def create_data(endpoint, payload):
    url = f"{base_url}/{endpoint}"
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None

def update_data(endpoint, id, payload):
    url = f"{base_url}/{endpoint}/{id}"
    
    try:
        response = requests.put(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None

def delete_data(endpoint, id):
    url = f"{base_url}/{endpoint}/{id}"
    
    try:
        response = requests.delete(url)
        response.raise_for_status()
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return False

if __name__ == "__main__":
    print("Fetching all posts:")
    posts = get_all("posts")
    print(json.dumps(posts, indent=4))

    print("\nFetching a single post:")
    post = find_data("posts", 1)
    print(json.dumps(post, indent=4))

    print("\nCreating a new post:")
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    created = create_data("posts", new_post)
    print(json.dumps(created, indent=4))

    print("\nUpdating a post:")
    updated_post = {"id": 1, "title": "foo updated", "body": "bar updated", "userId": 1}
    updated = update_data("posts", 1, updated_post)
    print(json.dumps(updated, indent=4))

    print("\nDeleting a post:")
    deleted = delete_data("posts", 1)
    print(f"Deleted: {deleted}")