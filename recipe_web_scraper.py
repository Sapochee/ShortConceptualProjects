"""Code uses BeautifulSoup in order to retrieve the names of the recipes listed in "80 cheap dinner recipes" and prints it out
"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.delish.com/cooking/recipe-ideas/g3166/cheap-easy-recipes/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    recipe_names = [h2.text for h2 in soup.find_all('h2', class_='css-btou1l e1tmud0h8')]

    print(f'Found {len(recipe_names)} titles')

    for name in recipe_names:
        print(name)
else:
    print('Error fetching the webpage.')