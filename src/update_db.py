import requests
from db import PiBlogDatabase

db = PiBlogDatabase()

url = 'https://www.raspberrypi.org/wp-json/wp/v2/posts?per_page=100'

posts = True
page = 1

while posts:
    request = '{}&page={}'.format(url, page)
    posts = requests.get(request).json()
    for post in posts:
        slug = post['slug']
        title = post['title']['rendered']
        pub_date = post['date']
        db.insert_post(slug, title, pub_date)
    page += 1