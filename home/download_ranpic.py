import requests
import os
import string
import secrets

def generate_random_string(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))



def download_random_image():
    r=generate_random_string(10)
    url = f"https://robohash.org/{r}"
    response = requests.get(url)
    path=f"media/photos/{r}.svg"
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
        return path
        print("Image saved as random_image.svg")
    else:
        print("Could not download image")
        return f"media/photos/random_image.svg"
