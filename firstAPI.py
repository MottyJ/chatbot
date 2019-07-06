import requests

def new_joke():
    get_joke = requests.get('https://api.chucknorris.io/jokes/random')
    return get_joke.value